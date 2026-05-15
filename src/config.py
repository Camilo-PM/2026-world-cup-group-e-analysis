from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed"
FINAL_DATA_PATH = BASE_DIR / "data" / "final"

TEAMS = {
    "United States": [
        "data/raw/html/united_states.html",
        "data/raw/html/united_states_2025.html"
    ],
    "Paraguay": [
        "data/raw/html/paraguay.html",
        "data/raw/html/paraguay_2025.html"
    ],
    "Australia": [
        "data/raw/html/australia.html",
        "data/raw/html/australia_2025.html"
    ],
    "Türkiye": [
        "data/raw/html/turkiye.html",
        "data/raw/html/turkiye_2025.html"
    ]
}