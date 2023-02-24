from strenum import StrEnum
from enum import Enum


class PericiaNiveisDeTreinamento(StrEnum):
    TREINADO = "treinado"


class PericiaModificador(Enum):
    TREINADO = 2
    ADEPTO = 5


class Pericia(StrEnum):
    teste = "Teste"
    OFFICE_1 = "office_1"
