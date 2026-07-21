from dataclasses import dataclass
from pathlib import Path


@dataclass
class Document:
    """
    Represents a single loaded document.
    """

    file_name: str
    file_path: Path
    text: str
    page_count: int