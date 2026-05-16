from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed"
FINAL_DATA_PATH = BASE_DIR / "data" / "final"

# ======================================
# CONFIGURACIÓN GRUPO E
# ======================================

TEAMS = {
    "Germany": [
        "data/raw/html/germany.html"
    ],

    "Ecuador": [
        "data/raw/html/ecuador.html"
    ],

    "Ivory Coast": [
        "data/raw/html/ivory_coast.html"
    ],

    "Curacao": [
        "data/raw/html/curacao.html"
    ]
}