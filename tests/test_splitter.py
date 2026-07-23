from pathlib import Path

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

    splitter = TextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )

    chunks = splitter.split(document)

    assert len(chunks) == 3

    assert chunks[0].chunk_id == 0
    assert chunks[1].chunk_id == 1
    assert chunks[2].chunk_id == 2

    assert chunks[0].start_index == 0
    assert chunks[1].start_index == 450
    assert chunks[2].start_index == 900