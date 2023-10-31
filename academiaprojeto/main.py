from classes import *
import os
import time as timer

def encerrando():
            print("encerrando sistema . ")
            timer.sleep (0.5)
            print("encerrando sistema . .  ")
            timer.sleep (0.5)
            print ("encerrando sistema . . .")
            timer.sleep (0.5)
            print ("encerrando sistema . . . .")
            timer.sleep (0.5)
            print ("encerrado!")           
def obter_escolha():
    while True:
        exibir_menu()

        escolha = input("Digite sua resposta = ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 0 <= escolha <= 5:
                return escolha
        os.system('cls')
        print("Escolha inválida. Digite um número entre 0 e .")
def exibir_menu():
    menu = """
Projeto academia

0 - exit
1 - cadastrar aluno
2 - mostrar todos alunos cadastrados
3 - Mostrar instrutores
4 - opção de passar pela catraca da academia
5 - remover alunos

"""
    print(menu)




if __name__ == "__main__":
    gym = academia()
    while True:
        escolha = obter_escolha()

        if escolha == 0:
            encerrando()
            break
        elif escolha == 1:
            print("cadastrando alunos. . .")
            timer.sleep (0.5)
            gym.novoAluno()
        elif escolha == 2:
            print("mostrar Alunos\n\n")
            gym.mostrarAlunos()

        elif escolha == 3:
            print("mostrar instrutores\n\n")
            gym.mostrarInstru()

        elif escolha == 4:
            print("passar pela catraca\n\n")
            gym.passarCatraca()
        else:
            print("remover alunos")
            gym.removerAluno()