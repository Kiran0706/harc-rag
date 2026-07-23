from harc_rag.retrieval.interfaces import Retriever


class DenseRetriever(Retriever):

    def __init__(
        self,
        embedding_service,
        vector_store,
    ):
        self.embedding_service = embedding_service
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        k: int = 5,
    ):
        raise NotImplementedError