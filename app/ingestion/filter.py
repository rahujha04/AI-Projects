from pathlib import Path

class FileFilter:
    IGNORED_DIRECTORIES = {
        ".git", 
        ".venv", 
        "__pycache__",
        "build",
        "dist",
        "node_modules",
    }

    @classmethod
    def should_include(cls, path: Path) -> bool:
        for parent in path.parents:
            if parent.name in cls.IGNORED_DIRECTORIES:
                return False
        if path.name.startswith("."):
            return False
        return True

