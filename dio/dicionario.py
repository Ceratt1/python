# pessoa = dict (nome = "guilherme", idade = 28)

# print(pessoa)

# contatos = {

#     "gabriel" : {"nome": "gabriel", "idade" : 19, "tel" : "555"},
#     "robert" : {"nome": "robert", "idade" : 21, "tel" : "666", "extra" : {"a" : 2}}

# }

# # print (contatos)

# # a = input("digite o nome da pessoa que deseja puxar: ").lower()
# # b = input("o que deseja saber: ").lower()

# # print (contatos[a][b])

# for x, y in contatos.items():
#     print (x,"=>", y)   
# Sua variável de texto



print ("\n" *100)


pessoa = dict.fromkeys(["nome", "idade"], "####")


print (pessoa)

print(pessoa.get("chave", "não encontrado"))






