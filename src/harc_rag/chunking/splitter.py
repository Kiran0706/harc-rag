from harc_rag.chunking.exceptions import InvalidChunkConfigurationError
from harc_rag.chunking.models import Chunk
from harc_rag.document.models import Document


class TextSplitter:
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        if chunk_size <= 0:
            raise InvalidChunkConfigurationError(
                "chunk_size must be greater than 0"
            )

        if chunk_overlap < 0:
            raise InvalidChunkConfigurationError(
                "chunk_overlap cannot be negative"
            )

        if chunk_overlap >= chunk_size:
            raise InvalidChunkConfigurationError(
                "chunk_overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, document: Document) -> list[Chunk]:
        chunks = []

        start = 0
        chunk_id = 0

        while start < len(document.text):
            end = min(start + self.chunk_size, len(document.text))

            chunks.append(
                Chunk(
                    chunk_id=chunk_id,
                    text=document.text[start:end],
                    start_index=start,
                    end_index=end,
                    metadata=document.metadata.copy(),
                )
            )

            chunk_id += 1
            start += self.chunk_size - self.chunk_overlap

        return chunks