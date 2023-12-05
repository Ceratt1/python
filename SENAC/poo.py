import os as sistema;
from datetime import datetime
horario_atual = datetime.now()
sistema.system('cls')
# class pessoa:
#     def __init__(self, nome, trfAtribuida):
#         self.nome = nome
#         self.TarefaAtribuida = trfAtribuida

# class usuario (pessoa):
#     def __init__(self, nome, trfAtribuida):
#         super().__init__(nome, trfAtribuida)




class tarefa:
    def __init__(self, tituloTarefa, descTarefa, sttsTarefa, data):
        self.titulo = tituloTarefa
        self.descricao = descTarefa
        self.status = sttsTarefa
        self.data = data
    def alterarStatus(self):
        pass
    def attDesc (self):
        pass
    def finalizarTarefa (self):
        pass
    def __str__(self) -> str:
        return self.titulo

a = tarefa("penis", "chupar penis", True, horario_atual)