from pathlib import Path

from harc_rag.chunking.character_strategy import CharacterChunkingStrategy
from harc_rag.chunking.splitter import TextSplitter
from harc_rag.document.models import Document


def test_splitter():
    document = Document(
        file_name="sample.pdf",
        file_path=Path("sample.pdf"),
        text="A" * 1200,
        page_count=1,
        metadata={},
    )

    strategy = CharacterChunkingStrategy(
        chunk_size=500,
        chunk_overlap=50,
    )

    splitter = TextSplitter(strategy)

    chunks = splitter.split(document)

    assert len(chunks) == 3