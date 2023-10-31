import json
import os

os.system('cls')
import json

alunos = {"joao": {"idade": 29, "senha": 201303}}

# Salve os dados iniciais no arquivo JSON
with open("alunosdata.json", "w") as alunosData:
    json.dump(alunos, alunosData, indent=4)

alunos = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "Outroville"
}

# Abra o arquivo JSON no modo de leitura e escrita ("r+")
with open("alunosdata.json", "r+") as json_file:
    data = json.load(json_file)


    # Adicione os novos dados ao dicionário
    data["maria"] = alunos

    # Volte ao início do arquivo e escreva o JSON atualizado
    json_file.seek(0)
    json_file.truncate()
    json.dump(data, json_file, indent=4)

print(data)  # Exibe o dicionário atualizado
