from pathlib import Path


class LanguageDetector:
    EXTENSION_MAPPING = {
        ".py": "Python",
        ".cpp": "C++",
        ".cc": "C++",
        ".cxx": "C++",
        ".c": "C",
        ".h": "C Header",
        ".hpp": "C++ Header",
        ".sv": "SystemVerilog",
        ".v": "Verilog",
        ".md": "Markdown",
        ".txt": "Text",
        ".json": "JSON",
        ".yaml": "YAML",
        ".yml": "YAML",
    }

    @classmethod
    def detect(cls, path: Path) -> str:
        return cls.EXTENSION_MAPPING.get(
            path.suffix.lower(),
            "Unknown",
        )