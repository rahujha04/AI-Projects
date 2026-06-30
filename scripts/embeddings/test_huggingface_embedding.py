import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.embeddings.huggingface_embedding import HuggingFaceEmbeddingModel

from app.retrieval.similarity import CosineSimilarity

model = HuggingFaceEmbeddingModel()

text1 = "How do I optimize C++ code?"

text2 = "How can I improve C++ performance" 

text3 = "How do I bake a chocolate cake?"

e1 = model.embed(text1)
e2 = model.embed(text2)
e3 = model.embed(text3)

print(
    CosineSimilarity.compute(e1, e2)
)

print(
    CosineSimilarity.compute(e1, e3)
)