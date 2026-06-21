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
    for y in '87654321':    # Loop começando pela esquerda até a direita 
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

