from typing import List

from pydantic import BaseModel


class Message(BaseModel):
    player: str
    message: str


class Chat(BaseModel):
    name: str
    history: List[Message]
