mensagem = 'A arte está presente o tempo todo com nós, basta olharmos ela nos olhos e sorrir'
contar = {}

for characteres in mensagem:
    contar.setdefault(characteres, 0) # chave correspondente ao caractere exista no dicionário contar
    # atribuido 0 caso ainda não exista e evita o erro tipo KeyError
    contar[characteres] = contar[characteres] + 1 # 
print(contar)
