import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.chunking.models import Chunk
from app.embeddings.huggingface_embedding import HuggingFaceEmbeddingModel
from app.ingestion.models import Document
from app.retrieval.vector_store import VectorStore

model = HuggingFaceEmbeddingModel()

texts = [
    "C++ optimization techniques",
    "Python machine learning",
    "Chocolate cake recipe",
]

chunks = []

embeddings = []

for text in texts:
    doc = Document(
        path=Path("dummy.txt"),
        content=text,
        language="Text",
        size=len(text),
    )

    chunk = Chunk(
        document=doc,
        text=text,
        start=0,
        end=len(text),
    )

    chunks.append(chunk)
    embeddings.append(model.embed(text))

store = VectorStore()
store.build(chunks, embeddings)

query = "How can I improve C++ performance?"

query_embedding = model.embed(query)

results = store.search(query_embedding)

for chunk, score in results:
    print(f"{score:.3f} -> {chunk.text}")