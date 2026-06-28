import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.ingestion.models import Document

doc = Document(
    path=Path("main.cpp"),
    content="int main() {}",
    language="cpp",
    size=15
)

print(doc)