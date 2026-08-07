from harc_rag.uncertainty.threshold import AdaptiveThreshold


def test_easy_question():

    threshold = AdaptiveThreshold()

    value = threshold.calculate(
        "What is TCP?"
    )

    assert value == 0.80


def test_complex_question():

    threshold = AdaptiveThreshold()

    value = threshold.calculate(
        "Explain how adaptive verification reduces hallucination in conversational retrieval augmented generation."
    )

    assert value == 0.60