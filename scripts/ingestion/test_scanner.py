import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.ingestion.scanner import RepositoryScanner

scanner = RepositoryScanner(Path("."))

files = scanner.scan()

for file in files:
    print(file)