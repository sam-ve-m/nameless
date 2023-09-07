from functools import wraps
from typing import Union

import wsproto.utilities
from fastapi import WebSocketDisconnect, APIRouter

subscriptions = {}

class WebsocketRouter(APIRouter):
    last_url: str

    def new_websocket_route(self, url: str):
        self.last_url = url

        def wrapper_function(function):
            @wraps(function)
            async def websocket_function(*args, **kwargs):
                websocket = kwargs['websocket']
                player = kwargs['player']
                try:
                    await websocket.accept()
                    player_subscriptions = subscriptions.get(player, {})
                    player_subscriptions[self.last_url] = websocket
                    subscriptions[player] = player_subscriptions
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

    @staticmethod
    async def get_active_websocket_subscriptions() -> list:
        return list(subscriptions.keys())

    async def publish_json(self, message: Union[dict, list], websocket_to_ignore=None):
        sockets = (player_subscriptions[self.last_url] for player_subscriptions in  subscriptions.values())
        for socket in sockets:
            if socket != websocket_to_ignore:
                await socket.send_json(message)
