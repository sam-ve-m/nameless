import asyncio

from fastapi import WebSocket
from fastapi.websockets import WebSocketState

from src.routes.base.websocket import WebsocketRouter
from src.services.chat.service import ChatService
from src.services.dados.service import DadosService

dados_route = WebsocketRouter()
asyncio.run(DadosService.subscribe_to_watch_dados_rolados(
    publish_message_callback=dados_route.publish_json
))


@dados_route.new_websocket_route("/ws/dados/{player}")
async def dados(websocket: WebSocket, player: str):
    while websocket.client_state == WebSocketState.CONNECTED:
        received = await websocket.receive_json()
        try:
            modificador = int(received["modificador"] or 0)
        except ValueError:
            continue
        resultado = await DadosService.rolar_d20(
            modificador, received['atributo'], received.get("pericia"), player
        )
        await ChatService.save_message(resultado["mensagem"])
        await DadosService.publish_dado_rolado(resultado)


__all__ = dados_route,
