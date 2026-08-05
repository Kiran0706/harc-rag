from harc_rag.evaluation.metrics import (
    recall_at_k,
    mean_reciprocal_rank,
)


class RetrievalEvaluator:

    def evaluate(
        self,
        retrieved: list[int],
        relevant: list[int],
    ):

        return {
            "Recall@1": recall_at_k(
                retrieved,
                relevant,
                1,
            ),
            "Recall@3": recall_at_k(
                retrieved,
                relevant,
                3,
            ),
            "MRR": mean_reciprocal_rank(
                retrieved,
                relevant,
            ),
        }