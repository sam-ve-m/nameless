import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import nest_asyncio

nest_asyncio.apply()


from src.routes.chat.route import chat_route
from src.routes.dados.route import dados_route
from src.routes.imagem.route import images_route
from src.routes.personagens.route import personagens_route
from src.routes.player.route import player_route, rota_ficha_do_jogador


app = FastAPI()

app.mount("/static-js", StaticFiles(directory="src/static/javascript"), name="static-js")
app.mount("/static-css", StaticFiles(directory="src/static/css"), name="static-css")
app.mount("/images-files", StaticFiles(directory="src/static/images"), name="images-files")


app.include_router(dados_route)
app.include_router(chat_route)
app.include_router(player_route)
app.include_router(images_route)
app.include_router(personagens_route)
app.include_router(rota_ficha_do_jogador)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(
        app,
        port=3334,
    )
