import asyncio

from fastapi import Request, APIRouter, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.websockets import WebSocketState

from src.routes.base.websocket import WebsocketRouter
from src.services.jogador.service import JogadorService

player_templates = Jinja2Templates(directory="src/static/player")


player_route = APIRouter()


@player_route.get("/player/{player}")
def details(request: Request, player: str):
    if player == "mestre":
        return player_templates.TemplateResponse("mestre.html", {"request": request, "player": player})
    return player_templates.TemplateResponse("player.html", {"request": request, "player": player})

@player_route.get("/")
def guest(request: Request):
    return player_templates.TemplateResponse("player.html", {"request": request, "player": "Guest"})


rota_ficha_do_jogador = WebsocketRouter()
mudanca_em_jogadores = {}


@rota_ficha_do_jogador.new_websocket_route("/ws/ficha/{player}")
async def ficha(websocket: WebSocket, player: str):
    jogador = await JogadorService.pegar_jogador("teste")
    await websocket.send_json(jogador)
    while True:
        while not mudanca_em_jogadores.get(player) and websocket.client_state == WebSocketState.CONNECTED:
            await asyncio.sleep(1)
        if websocket.client_state != WebSocketState.CONNECTED:
            break
        jogador = await JogadorService.pegar_jogador(player)
        await websocket.send_json(jogador)
        mudanca_em_jogadores[player] = False


__all__ = player_route, rota_ficha_do_jogador
