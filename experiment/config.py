import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
MAX_IMAGE_SIZE = int(float(os.getenv("MAX_IMAGE_SIZE_MB", "50")) * 1024 * 1024)

OUTPUT_DIR = os.getenv("OUTPUT_DIR", os.path.join("experiment", "output"))
CSV_DIR = os.path.join(OUTPUT_DIR, "csv")
JS_OUT = os.path.join(OUTPUT_DIR, "csv_data.generated.js")

