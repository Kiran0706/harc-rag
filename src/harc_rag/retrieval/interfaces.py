from abc import ABC, abstractmethod

from harc_rag.retrieval.models import RetrievalResult


class Retriever(ABC):

    @abstractmethod
    def retrieve(
        self,
        query: str,
        k: int = 5,
    ) -> list[RetrievalResult]:
        """Retrieve the top-k relevant chunks."""