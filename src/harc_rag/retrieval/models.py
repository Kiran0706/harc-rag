from dataclasses import dataclass
from harc_rag.chunking.models import Chunk


@dataclass
class RetrievalResult:
    chunk: Chunk
    score: float