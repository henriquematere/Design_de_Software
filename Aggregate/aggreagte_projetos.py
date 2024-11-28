from dataclasses import dataclass, field
from uuid import uuid4
from datetime import date, datetime
from enum import Enum

class Prioridade(Enum):
    BAIXA = 0
    MEDIA = 10
    ALTA = 2

class Status(Enum):
    ABERTA = 0
    FECHADA = 1

@dataclass
class Tarefa: # entidade secundaria do aggregate
    descricao: str
    prazo: date
    prioridade: Prioridade
    status: Status
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
        if (self.prazo < datetime.now()):
            raise ValueError("Prazo deve ser em uma data futura")
        
    def marcar_como_concluida(self):
        pass

    def alterar_prioridade(self, nova_prioridade:Prioridade):
        pass

@dataclass
class Projeto: # entidade raiz do aggregate
    nome: str
    descricao: str
    tarefas: list[Tarefa] # Tipado como lista de Tarefa
    id: str = field(default_factory=lambda: str(uuid4()))

    def adicionar_tarefa(self, descricao: str, prazo:date, prioridade:Prioridade):
        pass

    def remover_tarefa(self, tarefa_id):
        pass

p1.adicionar_tarefa(
    descricao='Testar o software',
    prazo=date(2022, 12, 31),
    prioridade=Prioridade.ALTA
)