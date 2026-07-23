from abc import ABC, abstractmethod

from harc_rag.chunking.models import Chunk
from harc_rag.embedding.models import Embedding


class EmbeddingModel(ABC):

    @abstractmethod
    def embed(self, chunks: list[Chunk]) -> list[Embedding]:
        raise NotImplementedError