from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cliente:

    # Generated on Register
    _id: str

    email: str
    password: str

    # Generated on Register
    date: datetime

@dataclass
class Procedimento:

    _id: str
    nome: str
    descricao: str

    valor: float

@dataclass
class Agendamento:

    _id: str

    cliente: Cliente

    procedimento: Procedimento

    date: datetime

