import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.retrieval.similarity import CosineSimilarity

v1 = [1, 1]
v2 = [2, 2]
v3 = [1, 0]

print(CosineSimilarity.compute(v1, v2))
print(CosineSimilarity.compute(v1, v3))