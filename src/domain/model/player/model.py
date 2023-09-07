from typing import Dict, List

from pydantic import BaseModel, validator

from src.domain.enums.atributo.enum import Atributo
from src.domain.enums.pericia.enum import Pericia, PericiaNiveisDeTreinamento, PericiaModificador
from src.domain.enums.pericia_por_atributo.enum import PericiaPorAtributo


class PericiaDoJogador(BaseModel):
    nome: Pericia
    treinamento: PericiaNiveisDeTreinamento


class AtributoDoJogador(BaseModel):
    valor: int
    nome: Atributo
    pericias: List[PericiaDoJogador]

    @validator("pericias")
    def is_expertise_from_attribute(cls, pericias: List[PericiaDoJogador], values):
        atributo: Atributo = values["nome"]
        pericias_permitidas = PericiaPorAtributo[atributo.name].value
        for pericia in pericias:
            if pericia.nome not in pericias_permitidas:
                raise ValueError(
                    f"Perícia {pericia.value} "
                    + f"não permitida para atributo "
                    + f"{atributo.value}")
        return pericias


class Status(BaseModel):
    maximo: int = 0
    atual: int = 0


class Jogador(BaseModel):
    nome: str = ""
    raca: str = ""
    origem: str = ""
    caminho_da_foto: str = ""
    atributos: List[AtributoDoJogador] = []
    vida: Status = Status()
    esforco: Status = Status()
