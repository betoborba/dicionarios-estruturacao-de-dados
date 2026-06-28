import sys, copy 

# A constante STARTING_PIECES armazenará um dicionário que representa o tabuleiro
# com todas suas peças iniciais em cada casa do tabuleiro
STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'ww', 'd1': 'wQ', 'e1': 'wK', 'f1': 'ww',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'} 

# A variavél BOARD_TEMPLATE armazena uma string que servirá como modelo para o tabuleiro
# O programa pode inserir as istrings correspondentes as peças individuais nesse modelo antes de exibir

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""

WHITE_SQUARE = '||'
BLACK_SQUARE = '  '

# Os pares de chaves ({}) indicam os pontos da string em que as peças serão inseridas 
# O código dentro do loop for constrói a lista square, preenchendo com as strings apropriadas 
def print_chessboard(board):
    squares = []
    is_white_square = True # Valor Booleano controla quais casas são brancas e quais pretas 
    for y in '87654321':    # Loop começando pela esquerda até a direita in range 
        for x in 'abcdefgh': # Nesses dois loops as variáveis x e y assum os caract das strings 
            # Exibe (x, y, is_white_square) # Debug: Exibe as coordenadas
            if x + y in board.keys(): # Verifica se existe no dicionario
                squares.append(board[x + y]) # As strings são concatenadas para formar ex. a8
            else: 
                if is_white_square:
                    squares.append(WHITE_SQUARE) # Se a casa não tiver presente como chave o código adiciona a lista string casa vazia 
                else: 
                    squares.append(BLACK_SQUARE)
                is_white_square = not is_white_square #Após processar a casa atual o codigo alterna o valor booleano invertendo de Tru para False
            is_white_square = not is_white_square

    print(BOARD_TEMPLATE.format(*squares)) # Sintaxe do asterisco para passar os argumentos individual 

print('Interactive Chessboard')
print('by Me')
print()
print('Pieces:')
print(' w - White, b - Black')
print(' p - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
print('Commands: ')
print(' move e2 e4 - Moves the piece at e2 to e4')
print(' remove e2 - Removes the piece at e2' )
print(' set e2 wP - Sets squares e2 to a white pawn')
print(' reset - Resets pieces back to their starting squares')
print(' clear - Clears the entire board')
print(' fill wp - Fills entire board white pawns.')
print(' quit - Quits the program')


main_board = copy.copy(STARTING_PIECES) # a variavel recebe uma copia do dicionário ...que tem todas as posições iniciais do jogo
while True:    # A execuçao entre em um loop infinito permitindo o usuario digitar o comandos
    print_chessboard(main_board)
    response = input('> ').split()
    if response[0] == 'move':  # copia a peça presente  na casa 1 para a copia da casa 2 
        main_board[response[2]] = main_board[response[1]] 
        del main_board[response[1]]
    elif response[0] == 'remove':
        del main_board[response[1]]
    elif response[0] == 'set':
        main_board[response[1]] = response[2]
    elif response[0] == 'reset':
        main_board = copy.copy(STARTING_PIECES)
    elif response[0] == 'clear':
        main_board = {} # atribui o valor vazio  a main_board
    elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                main_board[x + y] = response[1]
    elif response[0] == 'quit':
      sys.exit()

