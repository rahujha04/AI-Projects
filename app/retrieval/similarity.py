import math


class CosineSimilarity:
    @staticmethod
    def compute(
        vector1: list[float],
        vector2: list[float],
    ) -> float:
        if len(vector1) != len(vector2):
            raise ValueError("Vectors must be of the same length.")

        dot = sum(a * b for a, b in zip(vector1, vector2))
        norm1 = math.sqrt(sum(x * x for x in vector1))
        norm2 = math.sqrt(sum(x * x for x in vector2))

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return dot / (norm1 * norm2)