aniversarios = {
    'Renata': 'maio 24', 'Guilherme': 'fevereiro 18', 'Samantha': 'novembro 8'}

while True:
    print('Entre com o nome: (blank to quit)')
    nome = input()
    if nome == '':
        break

    if nome in aniversarios: 
        print(aniversarios[nome] + ' hoje é o seu aniversario ' + nome)
    else:
        print('Eu não tenho nenhuma informação sobre ' + nome)
        print('Qual é a data do aniversario?')
    dia = input()
    aniversarios[nome] = dia
    print('dia do aniversário incluido com sucesso na base')
 