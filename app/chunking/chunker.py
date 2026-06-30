from app.chunking.models import Chunk
from app.ingestion.models import Document


class RecursiveCharacterChunker:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, document: Document) -> list[Chunk]:
        chunks = []
        text = document.content
        start = 0

        while start < len(text):
            end = min(start + self.chunk_size, len(text))

            chunk = Chunk(
                document=document,
                text=text[start:end],
                start=start,
                end=end,
            )

            chunks.append(chunk)
            start += self.chunk_size - self.chunk_overlap

        return chunks
