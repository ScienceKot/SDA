chess_board = []
number_of_stripes = 0
f = open('7A.txt', 'r')
for line in f:
    chess_board.append(list(line[:-1]))
for row in chess_board:
    if set(row) == set(['B']):
        number_of_stripes+=1
inversed_board = [[chess_board[i][j] for i in range(len(chess_board))] for j in range(len(chess_board[0]))]
for row in inversed_board:
    if set(row) == set(['B']):
        number_of_stripes+=1
print(number_of_stripes)