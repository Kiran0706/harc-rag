from harc_rag.routing.cost import CostEstimator


def test_cost():

    estimator = CostEstimator()

    cost = estimator.estimate(

        answer="TCP uses a three-way handshake.",

        context="TCP establishes a connection using a three-way handshake.",

    )

    assert cost > 0