import asyncio
from contextlib import asynccontextmanager

from tinydb import TinyDB, Query

from src.domain.model.chat.model import Chat, Message
from src.repositories.base.tiny import TinyDbRepository


class ChatRepository(TinyDbRepository):
    table_name = "chat"
    locks = {}

    @classmethod
    @asynccontextmanager
    async def _lock_chat(cls, chat_name):
        if not (lock := cls.locks.get(chat_name)):
            lock = asyncio.Lock()
            cls.locks[chat_name] = lock
        async with lock:
            yield

    @classmethod
    async def get_chat_history(cls, chat_name: str) -> Chat:
        connection = cls._get_table()
        chats = connection.search(Query().name == chat_name)
        if not chats:
            chat = Chat(name=chat_name, history=[])
            connection.insert(chat.dict())
            return chat
        chat = chats[0]
        model = Chat(**chat)
        return model

    @classmethod
    async def save_chat_message(cls, chat_name: str, message: Message):
        connection = cls._get_table()
        async with cls._lock_chat(chat_name):
            chat = await cls.get_chat_history(chat_name)
            chat.history.append(message)
            connection.update(chat.dict(), Query().name == chat_name)
