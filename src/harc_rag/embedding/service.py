from harc_rag.chunking.models import Chunk
from harc_rag.embedding.interfaces import EmbeddingModel
from harc_rag.embedding.models import Embedding


class EmbeddingService:

    def __init__(self, model: EmbeddingModel):
        self.model = model

    def embed(self, chunks: list[Chunk]) -> list[Embedding]:
        return self.model.embed(chunks)