from dataclasses import dataclass

from app.ingestion.models import Document


@dataclass(slots=True)
class Chunk:
    document: Document
    text: str
    start: int
    end: int
