import asyncio
from functools import wraps
from typing import Union

import wsproto.utilities
from fastapi import WebSocketDisconnect, APIRouter


class WebsocketRouter(APIRouter):
    subscriptions: dict

    def new_websocket_route(self, url: str):
        subscriptions = {}
        self.subscriptions = subscriptions

        def wrapper_function(function):
            @wraps(function)
            async def websocket_function(*args, **kwargs):
                websocket = kwargs['websocket']
                player = kwargs['player']
                try:
                    await websocket.accept()
                    self.subscriptions[player] = websocket
                    await function(*args, **kwargs)
                    if player in subscriptions:
                        del subscriptions[player]
                except RuntimeError as error:
                    if "disconnect message" not in str(error):
                        raise error
                except (
                        WebSocketDisconnect,
                        wsproto.utilities.LocalProtocolError
                ):
                    if player in subscriptions:
                        del subscriptions[player]
            self.websocket(url)(websocket_function)
        return wrapper_function

    async def get_active_websocket_subscriptions(self) -> list:
        subscriptions = self.subscriptions
        return list(subscriptions.keys())

    async def publish_json(self, message: Union[dict, list], websocket_to_ignore=None):
        for socket in self.subscriptions.values():
            if socket != websocket_to_ignore:
                await socket.send_json(message)
