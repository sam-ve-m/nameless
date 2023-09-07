from fastapi import WebSocket
from fastapi.websockets import WebSocketState

from src.routes.base.websocket import WebsocketRouter
from src.services.images.service import ImageService

images_route = WebsocketRouter()


@images_route.new_websocket_route("/ws/images/{player}")
async def images(websocket: WebSocket, player: str):
    images = await ImageService.get_images(player)
    await websocket.send_json(images)
    while websocket.client_state == WebSocketState.CONNECTED:
        received = await websocket.receive_text()
        # message = MessageDto(player=player, message=str(received))
        # await ImageService.save_image(message)


__all__ = images_route,
