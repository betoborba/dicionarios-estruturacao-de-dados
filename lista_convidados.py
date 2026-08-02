todos_convidados = {'Laura': {'sanduiche': 5, 'tortas': 12},
                    'Katia': {'empanada': 3, 'maçã': 2},
                    'carol': {'copos': 3, 'torta de maçã': 1}}

def total_trouxe(convidados, item):
    num_trouxe = 0 
    for k, v in convidados.items(): # dentro da função o loop for K itera sobre os pares de chave-valor do dicionário
        num_trouxe = num_trouxe + v.get(item, 0) # A variável v é atribuida aos items e se existir irá somar esses itens
    return num_trouxe

print('Numero de itens que cada um trouxe:')
print(' - Maçã     '+ str(total_trouxe(todos_convidados, 'maçã')))
print(' - Copos    '+ str(total_trouxe(todos_convidados, 'copos')))
print(' - Tortas   '+ str(total_trouxe(todos_convidados, 'torta de maçã')))
print(' - Sanduiche  ' + str(total_trouxe(todos_convidados, 'sanduiche')))
print(' - Empadana ' + str(total_trouxe(todos_convidados, 'empanada')))