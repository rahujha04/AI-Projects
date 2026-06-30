import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.embeddings.simple_embedding import SimpleEmbeddingModel

model = SimpleEmbeddingModel()

embedding = model.embed(
    "Artificial Intelligence is the future!"
)

print(len(embedding))

print(embedding)