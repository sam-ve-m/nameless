from fastapi import WebSocket
from fastapi.websockets import WebSocketState

from src.domain.dto.chat.dto import MessageDto
from src.routes.base.websocket import WebsocketRouter
from src.services.chat.service import ChatService

chat_route = WebsocketRouter()


@chat_route.new_websocket_route("/ws/chat/{player}")
async def chat(websocket: WebSocket, player: str):
    messages = await ChatService.get_history()
    await websocket.send_json(messages)
    while websocket.client_state == WebSocketState.CONNECTED:
        received = await websocket.receive_text()
        message = MessageDto(player=player, message=str(received))
        await ChatService.save_message(message)
        await chat_route.publish_json([message], websocket)


__all__ = chat_route,
