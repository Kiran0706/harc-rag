from abc import ABC, abstractmethod

from harc_rag.chunking.models import Chunk
from harc_rag.document.models import Document


class ChunkingStrategy(ABC):
    @abstractmethod
    def split(self, document: Document) -> list[Chunk]:
        """Split a document into chunks."""
        raise NotImplementedError