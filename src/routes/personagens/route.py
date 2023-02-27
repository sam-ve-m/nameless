import asyncio

from fastapi import WebSocket
from fastapi.websockets import WebSocketState

from src.routes.base.websocket import WebsocketRouter

personagens_route = WebsocketRouter()


@personagens_route.new_websocket_route("/ws/visible_characters/{player}")
async def personagens(websocket: WebSocket, player: str):
    while websocket.client_state == WebSocketState.CONNECTED:
        active_players = list(personagens_route.subscriptions.keys())
        await websocket.send_json(active_players)
        while await personagens_route.get_active_websocket_subscriptions() == active_players:
            await asyncio.sleep(0.1)


__all__ = personagens_route,
