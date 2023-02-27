import asyncio
from functools import wraps
from typing import Union

from fastapi import WebSocketDisconnect, APIRouter
from starlette.websockets import WebSocketState


class WebsocketRouter(APIRouter):
    subscriptions: dict

    def new_websocket_route(self, url: str):
        self.subscriptions = {}

        def wrapper_function(function):
            @wraps(function)
            async def websocket_function(*args, **kwargs):
                websocket = kwargs['websocket']
                player = kwargs['player']
                try:
                    await websocket.accept()
                    self.subscriptions[player] = websocket
                    await function(*args, **kwargs)
                    del self.subscriptions[player]
                except RuntimeError as error:
                    if "disconnect message" not in str(error):
                        raise error
                except WebSocketDisconnect:
                    del self.subscriptions[player]
            self.websocket(url)(websocket_function)
        return wrapper_function

    async def get_active_websocket_subscriptions(self) -> dict:
        subscriptions = self.subscriptions
        return subscriptions

    async def publish_json(self, message: Union[dict, list], websocket_to_ignore=None):
        for socket in self.subscriptions.values():
            if socket != websocket_to_ignore:
                await socket.send_json(message)
