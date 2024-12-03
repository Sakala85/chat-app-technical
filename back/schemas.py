from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    role: str  # 'user' or 'agent'
    content: str

class ChatHistory(BaseModel):
    chat_history: List[Message]
