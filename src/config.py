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
        "data/raw/html/germany.html",
        "data/raw/html/germany_2025.html",
        "data/raw/html/germany_2024.html"
    ],

    "Ecuador": [
        "data/raw/html/ecuador.html",
        "data/raw/html/ecuador_2025.html"
    ],

    "Ivory Coast": [
        "data/raw/html/ivory_coast.html",
        "data/raw/html/ivory_coast_2025.html"
    ],

    "Curacao": [
        "data/raw/html/curacao.html",
        "data/raw/html/curacao_2025.html"
    ]
}