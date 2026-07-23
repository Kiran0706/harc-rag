from harc_rag.chunking.character_strategy import CharacterChunkingStrategy
from harc_rag.chunking.models import Chunk
from harc_rag.document.models import Document


class WordChunkingStrategy(CharacterChunkingStrategy):
    def split(self, document: Document) -> list[Chunk]:
        chunks = []

        text = document.text

        start = 0
        chunk_id = 0

        while start < len(text):
            end = min(start + self.chunk_size, len(text))

            if end < len(text):
                while end > start and text[end] != " ":
                    end -= 1

                if end == start:
                    end = min(start + self.chunk_size, len(text))

            chunk_text = text[start:end].strip()

            chunks.append(
                Chunk(
                    chunk_id=chunk_id,
                    text=chunk_text,
                    start_index=start,
                    end_index=end,
                    metadata=document.metadata.copy(),
                )
            )

            chunk_id += 1

            start = max(
                end - self.chunk_overlap,
                start + 1,
            )

        return chunks