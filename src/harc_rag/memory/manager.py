from harc_rag.memory.models import Conversation, Message


class MemoryManager:

    def __init__(self):
        self.conversations = {}

    def create(self, conversation_id: str):

        conversation = Conversation(
            conversation_id=conversation_id
        )

        self.conversations[conversation_id] = conversation

        return conversation

    def add_message(
        self,
        conversation_id: str,
        role: str,
        content: str,
    ):

        conversation = self.conversations[conversation_id]

        conversation.messages.append(
            Message(
                role=role,
                content=content,
            )
        )

    def get(
        self,
        conversation_id: str,
    ) -> Conversation:

        return self.conversations[conversation_id]