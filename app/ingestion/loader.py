from pathlib import Path
from app.ingestion.models import Document
from app.ingestion.language_detector import LanguageDetector

class FileLoader:
    @staticmethod
    def load(path: Path) -> Document:
        content = path.read_text(
            encoding="utf-8", 
            errors="ignore",
        )

        language = LanguageDetector.detect(path)
        
        return Document(
            path=path,
            content=content,
            language=language,
            size=path.stat().st_size,
        )