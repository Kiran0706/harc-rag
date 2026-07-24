from harc_rag.chunking.models import Chunk
from harc_rag.generation.prompt_builder import PromptBuilder


def test_prompt_builder():

    chunks = [
        Chunk(
            chunk_id=1,
            text="TCP uses a three-way handshake.",
            start_index=0,
            end_index=31,
            metadata={},
        ),
        Chunk(
            chunk_id=2,
            text="UDP is connectionless.",
            start_index=32,
            end_index=54,
            metadata={},
        ),
    ]

    builder = PromptBuilder()

    prompt = builder.build(
        query="Explain TCP",
        chunks=chunks,
    )

    assert "TCP uses a three-way handshake." in prompt
    assert "Explain TCP" in prompt