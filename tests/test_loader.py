from harc_rag.document.loader import DocumentLoader


def test_loader():
    loader = DocumentLoader()

    doc = loader.load("data/sample.pdf")

    assert len(doc.text) > 0
    assert doc.page_count > 0