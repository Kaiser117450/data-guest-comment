import argparse
import os
import sys

# Support both package and direct script execution
try:
    if __package__ is None or __package__ == "":
        # Direct run: add current directory to sys.path
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from extract_gpt_vision import run_batch  # type: ignore
        from config import CSV_DIR, JS_OUT  # type: ignore
    else:
        from .extract_gpt_vision import run_batch
        from .config import CSV_DIR, JS_OUT
except Exception as _e:
    print("Import error:", _e)
    print("Coba jalankan: python -m experiment.run <folder_gambar> dari direktori project root.")
    raise


def main():
    ap = argparse.ArgumentParser(description="Batch extract guest comments from images using GPT Vision")
    ap.add_argument("input_dir", help="Folder berisi gambar formulir (jpg, png, webp, tiff, bmp)")
    args = ap.parse_args()

    grouped = run_batch(args.input_dir)
    print("\nOutput:")
    print(f"- CSV per gerai: {CSV_DIR}")
    print(f"- JS untuk dashboard: {JS_OUT}")
    print(f"- Gerai terdeteksi: {list(grouped.keys())}")


if __name__ == "__main__":
    main()

