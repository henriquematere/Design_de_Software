from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Email:
    valor: str

    def __post_init__(self):
        if (self.valida_email() == False):
            raise ValueError("E-mail inválido")
        
    def valida_email(self) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, self.valor):
        return True
    else:
        return False






email1 = Email('fulano@gmail.com')
email2 = Email('@fulano.gmail.com')
