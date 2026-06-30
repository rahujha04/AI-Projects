import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.ingestion.loader import FileLoader

document = FileLoader.load(Path("README.md"))

print(document.language)  