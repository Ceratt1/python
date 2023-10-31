import os
os.system('cls')
import time as timer


class academia:
    def __init__(self) -> None:
        self.alunos = {}
        self.instrutores = {}
    def novoAluno(self):
        nome = input("digite seu nome: ")
        idade = int(input("digite sua idade: "))
        senha = int(input("digite sua data de nascimento: "))
        self.alunos[nome] = {"idade" : idade, "senha" : senha}
    def novoInstrutor(self):
        nome = input("digite seu nome: ")
        idade = int(input("digite sua idade: "))
        self.instrutores[nome] = {"idade" : idade, "senha" : True}
    def mostrarAlunos(self):
        for nome, idade in self.alunos.items():
            print (f"aluno: {nome}")
    def mostrarInstru(self):
        for x, y in self.instrutores.items():
            print (f"instrutor : {x}")
    def removerAluno(self):
        for x in self.alunos:
            nome = input("digite o nome do aluno que deseja remover: ")
            del self.alunos[nome]
    def passarCatraca(self):
        for x in self.alunos:

            senha = int(input("digite sua senha: "))
            user = ""
            for user, valores in self.alunos.items():
                if valores["senha"] == senha:
                    print(f"Bom treino {user}!")
                    break

                else:
                    pass
    def __str__(self) -> str:
        return "academia do ceratti"


