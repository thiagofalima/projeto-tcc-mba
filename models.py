from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Cliente:

    # Generated on Register
    _id: str

    name: str
    nickname: str
    email: str

    # Generated on Register
    date: datetime

@dataclass
class Agendamento:

    _id: str

    cliente: Cliente

    date: datetime

