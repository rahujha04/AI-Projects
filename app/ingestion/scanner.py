from pathlib import Path

from app.ingestion.filter import FileFilter


class RepositoryScanner:
    def __init__(self, root_path: Path):
        self.root_path = root_path

    # def scan(self) -> list[Path]:
    #     return [
    #         path
    #         for path in self.root_path.rglob("*")
    #         if path.is_file()
    #     ]
    def scan(self) -> list[Path]:
        return [
            path
            for path in self.root_path.rglob("*")
            if path.is_file()
            and FileFilter.should_include(path)
        ]