from harc_rag.routing.router import AdaptiveRouter


def test_cost_aware_router():

    router = AdaptiveRouter()

    decision = router.route(

        confidence=0.40,

        question="Explain TCP.",

        answer="TCP.",

        context="TCP uses a three-way handshake.",

    )

    assert decision.should_verify