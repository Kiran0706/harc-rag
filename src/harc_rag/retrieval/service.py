from harc_rag.retrieval.config import RetrievalConfig
from harc_rag.retrieval.conversation_retriever import ConversationRetriever


class RetrievalService:

    def __init__(
        self,
        retriever,
        config: RetrievalConfig | None = None,
    ):
        self.retriever = retriever
        self.config = config or RetrievalConfig()

        self.conversation_retriever = ConversationRetriever(
            retriever
        )

    def retrieve(self, query: str):

        return self.retriever.retrieve(
            query=query,
            k=self.config.top_k,
        )

    def retrieve_with_memory(
        self,
        conversation,
        query,
    ):

        return self.conversation_retriever.retrieve(
            conversation,
            query,
            k=self.config.top_k,
        )