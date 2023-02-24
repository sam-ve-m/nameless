from typing import TypedDict

from src.domain.dto.chat.dto import MessageDto


class DadosDto(TypedDict):
    valor: int
    modificador: int
    dado_natural: int
    mensagem: MessageDto
