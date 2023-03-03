import asyncio
from typing import Dict

from src.domain.dto.jogador.dto import JogadorDto, AtributoDoJogadorDto, PericiaDoJogadorDto, StatusDto
from src.domain.enums.pericia.enum import PericiaModificador
from src.domain.model.player.model import Jogador, AtributoDoJogador, PericiaDoJogador
from src.repositories.jogador.repository import JogadorRepository


class JogadorService:
    repository = JogadorRepository

    @classmethod
    async def pegar_jogador(cls, nome: str) -> JogadorDto:
        jogador = await cls.repository.pegar_jogador(nome)
        atributos, defesa, movimento, vida, esforco  = await asyncio.gather(
            cls._calcula_atributos(jogador),
            cls._calcula_defesa(jogador),
            cls._calcula_movimento(jogador),
            cls._calcula_vida(jogador),
            cls._calcula_esforco(jogador),
        )
        dto = JogadorDto(
            nome=jogador.nome,
            raca=jogador.raca,
            defesa=defesa,
            movimento=movimento,
            origem=jogador.origem,
            caminho_da_foto=jogador.caminho_da_foto,
            atributos=atributos,
            vida=vida,
            esforco=esforco,
        )
        return dto

    @staticmethod
    async def _calcula_defesa(jogador: Jogador) -> int:
        return 0

    @staticmethod
    async def _calcula_movimento(jogador: Jogador) -> int:
        return 0

    @classmethod
    async def _calcula_atributos(cls, jogador: Jogador) -> Dict[str, AtributoDoJogadorDto]:
        atributos_dtos = await asyncio.gather(*(
            cls._calcula_atributo(atributo)
            for atributo in jogador.atributos
        ))
        atributos_dto = {dto["nome"]: dto for dto in atributos_dtos}
        return atributos_dto

    @classmethod
    async def _calcula_atributo(cls, atributo: AtributoDoJogador) -> AtributoDoJogadorDto:
        pericias_dtos = await asyncio.gather(*(
            cls._calcula_pericia(pericia)
            for pericia in atributo.pericias
        ))
        pericias_dtos.insert(0, PericiaDoJogadorDto(
            nome="",
            treinamento="nenhum",
            modificador=0
        ))
        atributo_dto = AtributoDoJogadorDto(
            nome=atributo.nome.value,
            valor=atributo.valor,
            pericias=pericias_dtos,
            modificador=atributo.valor//2-5,
        )
        return atributo_dto

    @staticmethod
    async def _calcula_pericia(pericia: PericiaDoJogador) -> PericiaDoJogadorDto:
        pericia_dto = PericiaDoJogadorDto(
            nome=pericia.nome.value,
            treinamento=pericia.treinamento.value,
            modificador=PericiaModificador[pericia.treinamento.name].value
        )
        return pericia_dto

    @staticmethod
    async def _calcula_vida(jogador: Jogador) -> StatusDto:
        return StatusDto(
            atual=jogador.vida.maximo,
            maximo=jogador.vida.maximo,
        )

    @staticmethod
    async def _calcula_esforco(jogador: Jogador) -> StatusDto:
        return StatusDto(
            atual=jogador.esforco.atual,
            maximo=jogador.esforco.maximo,
        )
