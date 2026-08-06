from harc_rag.routing.router import AdaptiveRouter


def test_high_confidence():

    router = AdaptiveRouter()

    result = router.route(0.90)

    assert result.should_verify is False


def test_low_confidence():

    router = AdaptiveRouter()

    result = router.route(0.40)

    assert result.should_verify is True