from harc_rag.evaluation.evaluator import RetrievalEvaluator


def test_evaluation():

    evaluator = RetrievalEvaluator()

    metrics = evaluator.evaluate(

        retrieved=[5, 2, 8],

        relevant=[5],

    )

    assert metrics["Recall@1"] == 1.0

    assert metrics["Recall@3"] == 1.0

    assert metrics["MRR"] == 1.0