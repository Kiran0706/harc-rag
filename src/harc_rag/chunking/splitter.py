from harc_rag.chunking.models import Chunk
from harc_rag.chunking.strategies import ChunkingStrategy
from harc_rag.document.models import Document


class TextSplitter:
    def __init__(self, strategy: ChunkingStrategy):
        self.strategy = strategy

    def split(self, document: Document) -> list[Chunk]:
        return self.strategy.split(document)