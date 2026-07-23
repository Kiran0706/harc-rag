from dataclasses import dataclass, field
from typing import Any


@dataclass
class Embedding:
    chunk_id: int
    vector: list[float]
    metadata: dict[str, Any] = field(default_factory=dict)