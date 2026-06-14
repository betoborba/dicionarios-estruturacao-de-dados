caixa = {'furar': 'furadadeira', 'pregar': 'prego', 'bater': 'martelo' }


while True:
    print('O que vc precisa fazer para consertar? (enter para parar)')
    ferramenta = input()
    if ferramenta == '':
        break
    
    if ferramenta in caixa:
        print(caixa[ferramenta] + ' está pronta para o uso ' + ferramenta)
    else:
        print('Eu não tenho essa ferramenta na ' + [caixa])
        print('Deseja incluir uma nova ferramenta?')
    itenNovo = input()
    caixa[ferramenta] = itenNovo
    print('Iten Novo Cadastrado')
