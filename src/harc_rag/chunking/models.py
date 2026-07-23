from dataclasses import dataclass, field
from typing import Any


@dataclass
class Chunk:
    chunk_id: int
    text: str
    start_index: int
    end_index: int
    metadata: dict[str, Any] = field(default_factory=dict)