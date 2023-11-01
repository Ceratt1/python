class pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    def __str__(self) -> str:
        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])})"
    def mudarNome(self, nome):
        self.nome =nome
class jardineiro(pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
    def mostrar(self):
        pass
    



a = jardineiro("gabriel", 18)

a.mudarNome("joao")

print (a)