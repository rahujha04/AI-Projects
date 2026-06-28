from dataclasses import dataclass
from pathlib import Path

@dataclass(slots=True)

class Document:
    path: Path
    content: str
    language: str
    size: int #this is file size in bytes
    