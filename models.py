from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cliente:

    # Generated on Register
    _id: str

    name: str
    email: str
    password: str

    # Generated on Register
    register_date: datetime

@dataclass
class Procedimento:

    _id: str
    nome: str
    descricao: str

    valor: float

@dataclass
class Agendamento:

    _id: str

    cliente: str

    procedimento: str

    date: datetime.date

    time: datetime.time

    def convert_date(self):
        self.date = self.date.isoformat()

    def convert_time(self):
        self.time = self.time.isoformat()

