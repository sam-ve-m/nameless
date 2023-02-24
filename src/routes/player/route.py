import asyncio

from fastapi import Request, APIRouter, WebSocket
from fastapi.templating import Jinja2Templates

from src.routes.base.websocket import WebsocketRouter
from src.services.jogador.service import JogadorService

player_templates = Jinja2Templates(directory="src/static/player")


player_route = APIRouter()


@player_route.get("/player/{player}")
def details(request: Request, player: str):
    return player_templates.TemplateResponse("player.html", {"request": request, "player": player})


rota_ficha_do_jogador = WebsocketRouter()
mudanca_em_jogadores = {}


@rota_ficha_do_jogador.new_websocket_route("/ws/ficha/{nome}")
async def ficha(websocket: WebSocket, nome: str):
    jogador = await JogadorService.pegar_jogador("teste")
    await websocket.send_json(jogador)
    while True:
        while not mudanca_em_jogadores.get(nome):
            await asyncio.sleep(1)
        jogador = await JogadorService.pegar_jogador(nome)
        await websocket.send_json(jogador)
        mudanca_em_jogadores[nome] = False


__all__ = player_route, rota_ficha_do_jogador
