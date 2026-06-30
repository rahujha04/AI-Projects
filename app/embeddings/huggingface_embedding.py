try:
    from sentence_transformers import SentenceTransformer
except ImportError:  # pragma: no cover - optional dependency guard
    SentenceTransformer = None


class HuggingFaceEmbeddingModel:
    def __init__(self):
        if SentenceTransformer is None:
            raise ImportError(
                "sentence-transformers is required to use HuggingFaceEmbeddingModel."
            )

        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    def embed(self, text: str) -> list[float]:
        embedding = self.model.encode(text, normalize_embeddings=True)
        return embedding.tolist()