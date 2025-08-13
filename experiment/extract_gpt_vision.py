import os, io, re, json, base64, csv
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from PIL import Image
from openai import OpenAI
# Support both package and direct script execution
try:
    from .config import OPENAI_API_KEY, MODEL, MAX_IMAGE_SIZE, OUTPUT_DIR, CSV_DIR, JS_OUT
except Exception:
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from config import OPENAI_API_KEY, MODEL, MAX_IMAGE_SIZE, OUTPUT_DIR, CSV_DIR, JS_OUT  # type: ignore

PROMPT = (
    "Extract fields from this Indonesian customer feedback form. Return ONLY valid minified JSON.\n\n"
    "Required keys:\n"
    "- cabang: store/branch name (string; if not present infer from header or write \"-\")\n"
    "- nama: string\n"
    "- nomer_hp: string (digits only if possible)\n"
    "- alamat: string\n"
    "- rate_makanan: one of [\"Enak Sekali\",\"Enak\",\"Biasa\",\"Tidak Enak\",\"-\"]\n"
    "- rate_pelayanan: one of [\"Baik Sekali\",\"Baik\",\"Biasa\",\"Tidak Baik\",\"-\"]\n"
    "- rate_kenyamanan: one of [\"Nyaman Sekali\",\"Nyaman\",\"Biasa\",\"Tidak Nyaman\",\"-\"]\n"
    "- rate_kebersihan: one of [\"Bersih Sekali\",\"Bersih\",\"Biasa\",\"Tidak Bersih\",\"-\"]\n"
    "- kritik_saran: string\n\n"
    "Rules:\n"
    "- Prefer checkbox ticks/marks over nearby text.\n"
    "- Keep original spelling for free text.\n"
    "- If missing/unclear use \"-\".\n"
    "Return as: {\"cabang\":\"...\",\"nama\":\"...\",\"nomer_hp\":\"...\",\"alamat\":\"...\",\"rate_makanan\":\"...\",\"rate_pelayanan\":\"...\",\"rate_kenyamanan\":\"...\",\"rate_kebersihan\":\"...\",\"kritik_saran\":\"...\"}"
)

HEADERS = [
    "Nama",
    "No HP/WA",
    "Alamat",
    "Rate Makanan",
    "Rate Pelayanan",
    "Rate Kenyamanan",
    "Rate Kebersihan",
    "Kritik dan Saran",
]


class VisionExtractor:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def _optimize(self, path: str) -> bytes:
        with Image.open(path) as img:
            fmt = "JPEG" if img.format in ("PNG", "BMP", "TIFF", "WEBP") else (img.format or "JPEG")
            if fmt == "PNG":
                img = img.convert("RGB"); fmt = "JPEG"
            buf = io.BytesIO()
            img.save(buf, format=fmt, quality=90, optimize=True)
            data = buf.getvalue()
            if len(data) <= MAX_IMAGE_SIZE:
                return data
            quality = 85
            scale = 1.0
            while len(data) > MAX_IMAGE_SIZE and (quality >= 30 or scale > 0.25):
                if quality >= 30:
                    buf = io.BytesIO()
                    img.save(buf, format="JPEG", quality=quality, optimize=True)
                    data = buf.getvalue()
                    quality -= 10
                    continue
                scale *= 0.85
                w, h = int(img.width * scale), int(img.height * scale)
                img = img.resize((w, h), Image.Resampling.LANCZOS)
                buf = io.BytesIO()
                img.save(buf, format="JPEG", quality=70, optimize=True)
                data = buf.getvalue()
            return data

    def extract_one(self, image_path: str) -> Optional[Dict]:
        raw = self._optimize(image_path)
        b64 = base64.b64encode(raw).decode("utf-8")
        resp = self.client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": PROMPT},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
                    ],
                }
            ],
            temperature=0,
        )
        text = resp.choices[0].message.content.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]
        try:
            data = json.loads(text)
            data.setdefault("cabang", "-")
            data.setdefault("nama", "-")
            data.setdefault("nomer_hp", "-")
            data.setdefault("alamat", "-")
            for k in (
                "rate_makanan",
                "rate_pelayanan",
                "rate_kenyamanan",
                "rate_kebersihan",
                "kritik_saran",
            ):
                data.setdefault(k, "-")
            return data
        except Exception:
            return None

    def extract_batch(self, batch_items: List[Tuple[str, bytes]]) -> Optional[List[Dict]]:
        """Extract a batch of images in a single API call.

        batch_items: list of (filename, optimized_image_bytes)
        Returns list of dicts in the same order as input, or None on failure.
        """
        if not batch_items:
            return []

        content: List[Dict] = []
        names = [name for name, _ in batch_items]
        header = (
            "You will be given multiple images of Indonesian customer feedback forms. "
            "For EACH image, extract the required fields as described below and return a JSON array, "
            "one object per image, in the SAME ORDER as provided. Add a field 'source' with the file name.\n\n"
            + PROMPT + "\n\nReturn ONLY a valid minified JSON array like: [{...},{...},...]."
        )
        content.append({"type": "text", "text": header})
        for idx, (name, data) in enumerate(batch_items, 1):
            b64 = base64.b64encode(data).decode("utf-8")
            content.append({"type": "text", "text": f"Image {idx}: {name}"})
            content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}})

        resp = self.client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": content}],
            temperature=0,
        )
        text = resp.choices[0].message.content.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]
        try:
            arr = json.loads(text)
            if not isinstance(arr, list):
                return None
            # normalize and ensure order length matches
            out: List[Dict] = []
            for i, obj in enumerate(arr):
                if not isinstance(obj, dict):
                    return None
                obj.setdefault("source", names[i] if i < len(names) else "-")
                obj.setdefault("cabang", "-")
                obj.setdefault("nama", "-")
                obj.setdefault("nomer_hp", "-")
                obj.setdefault("alamat", "-")
                for k in (
                    "rate_makanan",
                    "rate_pelayanan",
                    "rate_kenyamanan",
                    "rate_kebersihan",
                    "kritik_saran",
                ):
                    obj.setdefault(k, "-")
                out.append(obj)
            return out
        except Exception:
            return None


def group_rows_by_branch(rows: List[Dict]) -> Dict[str, List[List[str]]]:
    grouped: Dict[str, List[List[str]]] = {}
    for r in rows:
        branch = (r.get("cabang") or "-").strip() or "-"
        row = [
            r.get("nama", "-"),
            r.get("nomer_hp", "-"),
            r.get("alamat", "-"),
            r.get("rate_makanan", "-"),
            r.get("rate_pelayanan", "-"),
            r.get("rate_kenyamanan", "-"),
            r.get("rate_kebersihan", "-"),
            r.get("kritik_saran", "-"),
        ]
        grouped.setdefault(branch, []).append(row)
    return grouped


def write_csvs(grouped: Dict[str, List[List[str]]], out_dir: str = CSV_DIR):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    for branch, rows in grouped.items():
        fn = f"{re.sub(r'[^\w\- ]','', branch).strip().replace(' ', '_')}.csv"
        p = Path(out_dir) / fn
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(HEADERS)
            w.writerows(rows)


def write_js(grouped: Dict[str, List[List[str]]], js_path: str = JS_OUT):
    lines = ["const csvData = {\n"]
    for branch, rows in grouped.items():
        lines.append(f'    "{branch}": [\n')
        lines.append("        [\"" + "\", \"".join(HEADERS) + "\"],\n")
        for r in rows:
            escaped = [
                str(c).replace('"', '\\"').replace("\n", "\\n").replace("\r", "")
                for c in r
            ]
            lines.append("        [\"" + "\", \"".join(escaped) + "\"],\n")
        lines.append("    ],\n")
    lines.append("};\n")
    Path(js_path).parent.mkdir(parents=True, exist_ok=True)
    Path(js_path).write_text("".join(lines), encoding="utf-8")


def run_batch(input_dir: str, max_images_per_batch: int = 6, max_bytes_per_batch: int = 15*1024*1024) -> Dict[str, List[List[str]]]:
    vx = VisionExtractor()
    images: List[Path] = []
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp", "*.tif", "*.tiff", "*.bmp"):
        images += list(Path(input_dir).glob(ext))
    images = sorted(images)
    if not images:
        print("No images found.")
        return {}

    # Build optimized payloads first
    optimized: List[Tuple[str, bytes]] = []
    for i, p in enumerate(images, 1):
        try:
            data = vx._optimize(str(p))
            optimized.append((p.name, data))
        except Exception as e:
            print(f"Skip {p.name}: {e}")

    rows: List[Dict] = []
    # Batch by size and count
    batch: List[Tuple[str, bytes]] = []
    batch_bytes = 0
    total = len(optimized)
    processed = 0
    for name, data in optimized:
        # Decide if adding this image exceeds thresholds
        if (batch and (
            len(batch) >= max_images_per_batch or
            batch_bytes + len(data) > max_bytes_per_batch
        )):
            # send current batch
            idx_from = processed - len(batch) + 1
            idx_to = processed
            print(f"Batching {len(batch)} images [{idx_from}-{idx_to}] ...")
            res_list = vx.extract_batch(batch)
            if not res_list:
                # fallback per-image for this batch
                for bn, bd in batch:
                    print(f"  fallback: {bn}")
                    single = vx.extract_one(str(Path(input_dir)/bn))
                    if single:
                        single.setdefault("source", bn)
                        rows.append(single)
            else:
                rows.extend(res_list)
            batch = []
            batch_bytes = 0

        batch.append((name, data))
        batch_bytes += len(data)
        processed += 1

    # flush remaining
    if batch:
        print(f"Batching {len(batch)} images [last] ...")
        res_list = vx.extract_batch(batch)
        if not res_list:
            for bn, bd in batch:
                print(f"  fallback: {bn}")
                single = vx.extract_one(str(Path(input_dir)/bn))
                if single:
                    single.setdefault("source", bn)
                    rows.append(single)
        else:
            rows.extend(res_list)

    grouped = group_rows_by_branch(rows)
    write_csvs(grouped)
    write_js(grouped)
    return grouped

