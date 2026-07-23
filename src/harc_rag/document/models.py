from dataclasses import dataclass
from pathlib import Path
from typing import Any

@dataclass
class Document:
    file_name: str
    file_path: Path
    text: str
    page_count: int
    metadata: dict[str, Any]