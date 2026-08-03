from abc import ABC, abstractmethod

from harc_rag.memory.models import Conversation


class MemoryStore(ABC):

    @abstractmethod
    def save(self, conversation: Conversation):
        pass

    @abstractmethod
    def load(self, conversation_id: str) -> Conversation:
        pass