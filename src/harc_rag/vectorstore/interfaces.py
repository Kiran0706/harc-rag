from abc import ABC, abstractmethod

from harc_rag.embedding.models import Embedding
from harc_rag.vectorstore.models import SearchResult


class VectorStore(ABC):

    @abstractmethod
    def add(self, embeddings: list[Embedding]) -> None:
        """Add embeddings to the vector store."""

    @abstractmethod
    def search(
        self,
        query_vector: list[float],
        k: int = 5,
    ) -> list[SearchResult]:
        """Return the top-k most similar embeddings."""

    @abstractmethod
    def save(self, path: str) -> None:
        """Save the index."""

    @abstractmethod
    def load(self, path: str) -> None:
        """Load the index."""