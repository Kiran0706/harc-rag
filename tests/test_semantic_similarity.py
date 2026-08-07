from harc_rag.uncertainty.semantic_similarity import (
    SemanticSimilarity,
)


def test_similarity():

    semantic = SemanticSimilarity()

    score = semantic.similarity(

        "TCP uses a three-way handshake.",

        "TCP establishes a connection using a three-way handshake.",

    )

    assert score > 0.80