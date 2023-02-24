import asyncio
from random import randint
from typing import List

from src.domain.dto.chat.dto import MessageDto
from src.domain.dto.dados.dto import DadosDto


class DadosService:
    @classmethod
    async def rolar_d20(
            cls, modificador: int, atributo: str, pericia: str, jogador: str
    ) -> DadosDto:
        dado_natural = randint(1, 20)
        valor_final = dado_natural + modificador
        mensagem = await cls._mesagem_da_rolagem(
            valor_final, atributo, pericia, jogador
        )
        dados_dto = DadosDto(
            valor=valor_final,
            modificador=modificador,
            dado_natural=dado_natural,
            mensagem=mensagem
        )
        return dados_dto

    @staticmethod
    async def _mesagem_da_rolagem(
            valor_do_dado: int, atributo: str, pericia: str, jogador: str
    ) -> MessageDto:
        texto = f"<i>Rolei um <b>{valor_do_dado}</b> em <b>{atributo}</b>"
        if pericia:
            texto += f" com <b>{pericia}</b>"
        texto += "</i>."
        message = MessageDto(player=jogador, message=texto)
        return message

    dados_rolados: List[DadosDto] = []

    @classmethod
    async def subscribe_to_watch_dados_rolados(cls, publish_message_callback):
        asyncio.create_task(cls.watch_dados_rolados(
            publish_message_callback=publish_message_callback
        ))

    @classmethod
    async def watch_dados_rolados(cls, publish_message_callback):
        while True:
            while not cls.dados_rolados:
                await asyncio.sleep(0.1)
            system_message = cls.dados_rolados.pop(0)
            await publish_message_callback(system_message)

    @classmethod
    async def publish_dado_rolado(cls, message: DadosDto):
        cls.dados_rolados.append(message)
