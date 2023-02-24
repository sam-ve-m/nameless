from typing import TypedDict, Dict, List


class PericiaDoJogadorDto(TypedDict):
    nome: str
    treinamento: str
    modificador: int


class AtributoDoJogadorDto(TypedDict):
    nome: str
    valor: int
    modificador: int
    pericias: List[PericiaDoJogadorDto]


class JogadorDto(TypedDict):
    nome: str
    raca: str
    defesa: int
    origem: str
    movimento: int
    caminho_da_foto: str
    atributos: Dict[str, AtributoDoJogadorDto]
