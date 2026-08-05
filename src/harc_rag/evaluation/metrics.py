def recall_at_k(
    retrieved: list[int],
    relevant: list[int],
    k: int,
) -> float:

    retrieved_k = retrieved[:k]

    hits = sum(
        1
        for item in retrieved_k
        if item in relevant
    )

    return hits / len(relevant)
def mean_reciprocal_rank(
    retrieved: list[int],
    relevant: list[int],
) -> float:

    for rank, chunk_id in enumerate(retrieved, start=1):

        if chunk_id in relevant:

            return 1 / rank

    return 0.0