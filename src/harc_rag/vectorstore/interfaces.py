from abc import ABC, abstractmethod

from harc_rag.embedding.models import Embedding
from harc_rag.vectorstore.models import SearchResult


class VectorStore(ABC):

    @abstractmethod
    def add(self, embeddings: list[Embedding]) -> None:
        pass

    @abstractmethod
    def search(
        self,
        query_vector: list[float],
        k: int = 5,
    ) -> list[SearchResult]:
        pass

    @abstractmethod
    def save(self, path: str) -> None:
        pass

    @abstractmethod
    def load(self, path: str) -> None:
        pass