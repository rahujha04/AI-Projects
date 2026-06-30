import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.chunking.chunker import RecursiveCharacterChunker
from app.ingestion.loader import FileLoader

document = FileLoader.load(Path("README.md"))

chunker = RecursiveCharacterChunker(
    chunk_size=100, 
    chunk_overlap=20
    )

chunks = chunker.split(document)

for i, chunk in enumerate(chunks):
    print("=" * 80)
    print(f"Chunk {i}")
    print(f"Range: {chunk.start} - {chunk.end}")
    print(chunk.text)
