# Experiment: GPT Vision Extraction

Output:
- CSV per gerai: `experiment/output/csv/*.csv`
- JS: `experiment/output/csv_data.generated.js`

## Setup

```bash
cd experiment
python -m venv .venv
. .venv/Scripts/Activate.ps1  # PowerShell
pip install -r requirements.txt
```

Buat file `.env` di folder `experiment`:
```
OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-4o-mini
MAX_IMAGE_SIZE_MB=50
OUTPUT_DIR=experiment/output
```

## Jalankan

- Cara 1 (disarankan, dari project root):
```bash
python -m experiment.run "C:\\path\\ke\\folder_form"
```

- Cara 2 (langsung di folder experiment):
```bash
cd experiment
python run.py "C:\\path\\ke\\folder_form"
```

