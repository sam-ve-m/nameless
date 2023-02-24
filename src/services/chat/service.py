import asyncio
from typing import List

from src.domain.dto.chat.dto import MessageDto
from src.domain.model.chat.model import Message
from src.repositories.chat.repository import ChatRepository


class ChatService:
    repository = ChatRepository

    @classmethod
    async def get_history(cls, chat: str="general") -> list[MessageDto]:
        chat = await cls.repository.get_chat_history(chat)
        messages = chat.dict()["history"]
        return messages

    @classmethod
    async def save_message(cls, message: MessageDto, chat: str="general"):
        message_model = Message(**message)
        await cls.repository.save_chat_message(chat, message_model)
