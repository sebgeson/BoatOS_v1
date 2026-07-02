from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "boatos" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "boatos.log"


def log(message: str) -> None:
    line = f"{datetime.now().isoformat(timespec='seconds')} | {message}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
