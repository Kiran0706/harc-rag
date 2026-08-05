from harc_rag.retrieval.models import RetrievalResult


class ReciprocalRankFusion:

    def __init__(self, constant: int = 60):
        self.constant = constant

    def fuse(
        self,
        dense_results: list[RetrievalResult],
        bm25_results: list[RetrievalResult],
    ) -> list[RetrievalResult]:

        scores = {}

        for rank, result in enumerate(dense_results, start=1):

            chunk_id = result.chunk.chunk_id

            scores.setdefault(chunk_id, result)

            scores[chunk_id].score = (
                1 / (self.constant + rank)
            )

        for rank, result in enumerate(bm25_results, start=1):

            chunk_id = result.chunk.chunk_id

            if chunk_id not in scores:

                scores[chunk_id] = result

                scores[chunk_id].score = 0

            scores[chunk_id].score += (
                1 / (self.constant + rank)
            )

        return sorted(
            scores.values(),
            key=lambda x: x.score,
            reverse=True,
        )