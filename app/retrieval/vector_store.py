try:
    import faiss
except ImportError:  # pragma: no cover - optional dependency guard
    faiss = None

import numpy as np

from app.chunking.models import Chunk


class VectorStore:
    def __init__(self):
        self.index = None
        self.chunks = []

    def build(self, chunks, embeddings):
        if faiss is None:
            raise ImportError("faiss is required to use VectorStore.")

        vectors = np.array(embeddings, dtype="float32")
        self.chunks = chunks
        dimension = vectors.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(vectors)

    def search(self, embedding, k=3):
        if self.index is None:
            raise ValueError("VectorStore must be built before searching.")

        query = np.array([embedding], dtype="float32")
        scores, indices = self.index.search(query, k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            results.append((self.chunks[idx], float(score)))

        return results