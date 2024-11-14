from dataclasses import dataclass
import re

@dataclass(frozen=True)
class CPF:
    valor: str

    def __post_init__(self):
        novoValor = re.sub('\D', '', self.valor) # Tudo que for diferente de dígito, ira substituir por um vazio. Foi feito para aceitar CPF com pontos e traços.
        object.__setattr__(self, 'valor', novoValor)    # Uma forma de desviar da classe frozen e conseguir alterar o valor.
        if (self.valida_cpf() == False):
            raise ValueError("O CPF não é válido.")
        
    def __str__(self):
        return f"{self.valor[0:3]}.{self.valor[3:6]}.{self.valor[6:9]}-{self.valor[9:11]}"

    def valida_cpf(self) -> bool:
        cpf = "".join(re.findall("\d", str(self.valor)))
        if not cpf.isdigit() or len(cpf) != 11:
            return False
        cpf_valido = cpf[0:9]
        base = 10
        while len(cpf_valido) < 11:
            soma = 0
            for n in cpf_valido:
                soma += int(n) * base
                base -= 1
            digito = soma % 11
            if digito < 2:
                digito = 0
            else:
                digito = 11 - digito
            cpf_valido += str(digito)
            base = 11
        if cpf_valido == cpf:
            return True
        return False

# Código de exemplo
cpf1 = CPF("46606196051")
cpf2 = CPF("466.061.960-51")
print(cpf1)
print(cpf2)
