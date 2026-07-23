from dataclasses import dataclass

from harc_rag.embedding.models import Embedding


@dataclass
class SearchResult:
    embedding: Embedding
    score: float