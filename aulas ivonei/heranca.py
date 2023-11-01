class pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade



class jardineiro(pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
    def mostrar(self):
        pass

jardineiro = jardineiro("gabriel", 19)