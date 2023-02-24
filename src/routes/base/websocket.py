from functools import wraps
from typing import Union

from fastapi import WebSocketDisconnect, APIRouter


class WebsocketRouter(APIRouter):

    def new_websocket_route(self, url: str):
        self.subscriptions = []
        def wrapper_function(function):
            @wraps(function)
            async def websocket_function(*args, **kwargs):
                websocket = kwargs['websocket']
                try:
                    await websocket.accept()
                    self.subscriptions.append(websocket)
                    await function(*args, **kwargs)
                except RuntimeError as error:
                    if "disconnect message" not in str(error):
                        raise error
                except WebSocketDisconnect:
                    self.subscriptions.remove(websocket)
            self.websocket(url)(websocket_function)
        return wrapper_function

    async def publish_json(self, message: Union[dict, list], websocket_to_ignore=None):
        for socket in self.subscriptions:
            if socket != websocket_to_ignore:
                await socket.send_json(message)
