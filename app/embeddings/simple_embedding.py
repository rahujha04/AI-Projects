from collections import Counter


class SimpleEmbeddingModel:
    def embed(self, text: str) -> list[float]:
        """
        Create a simple normalized character-frequency embedding.
        """
        text = text.lower()

        counts = Counter(c for c in text if c.isalpha())

        total = sum(counts.values())

        if total == 0:
            return [0.0] * 26

        embedding = []

        for letter in "abcdefghijklmnopqrstuvwxyz":
            embedding.append(counts[letter] / total)

        return embedding