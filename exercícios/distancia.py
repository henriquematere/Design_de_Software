from dataclasses import dataclass
from enum import Enum

# Usamos Enum quando temos poucas opções. (Como este caso)

class Unit(Enum):
    METRO = "metros"
    KM = "quilômetros"
    MILHA = "milhas"

    def __str__(self):
        return self.value

@dataclass(frozen=True)
class Distance:
    valor: float
    unidade: Unit

    def __str__(self):
        return f"{self.valor} {self.unidade}"

d1 = Distance(valor=1.5, unidade=Unit.METRO)
d2 = Distance(valor=10, unidade=Unit.KM)
