from harc_rag.memory.context_builder import ContextBuilder
from harc_rag.retrieval.interfaces import Retriever
from harc_rag.retrieval.models import RetrievalResult
from harc_rag.memory.models import Conversation


class ConversationRetriever:

    def __init__(
        self,
        retriever: Retriever,
    ):
        self.retriever = retriever
        self.context_builder = ContextBuilder()

    def retrieve(
        self,
        conversation: Conversation,
        query: str,
        k: int = 5,
    ) -> list[RetrievalResult]:

        history = self.context_builder.build(conversation)

        search_query = f"""
Conversation:
{history}

Current Question:
{query}
"""

        return self.retriever.retrieve(
            search_query,
            k,
        )