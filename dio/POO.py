import os
os.system('cls')


class humano:
    def __init__(self, nome, idade, cpf) -> None:
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    def __str__(self) -> str:
        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])})"

p1 = humano("robert", 19, 222)

print(p1)