from pathlib import Path

from harc_rag.chunking.word_strategy import WordChunkingStrategy
from harc_rag.document.models import Document


def test_word_chunking():
    document = Document(
        file_name="sample.pdf",
        file_path=Path("sample.pdf"),
        text="Artificial Intelligence is transforming healthcare rapidly.",
        page_count=1,
        metadata={},
    )

    strategy = WordChunkingStrategy(
        chunk_size=20,
        chunk_overlap=5,
    )

    chunks = strategy.split(document)

    for chunk in chunks:
        assert not chunk.text.startswith(" ")
        assert not chunk.text.endswith(" ")