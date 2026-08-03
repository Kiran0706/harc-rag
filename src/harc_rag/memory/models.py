from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Message:
    role: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class Conversation:
    conversation_id: str
    messages: list[Message] = field(default_factory=list)