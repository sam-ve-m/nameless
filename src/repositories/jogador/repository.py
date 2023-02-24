from tinydb import Query

from src.domain.model.player.model import Jogador
from src.repositories.base.tiny import TinyDbRepository


class JogadorRepository(TinyDbRepository):
    table_name = "personagens"

    @classmethod
    async def pegar_jogador(cls, nome: str) -> Jogador:
        connection = cls._get_table()
        jogadores = connection.search(Query().nome == nome)
        if not jogadores:
            raise ValueError("Jogador não encontrado")
        jogador = jogadores[0]
        model = Jogador(**jogador)
        return model
