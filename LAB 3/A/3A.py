# I use this dictionary to convert letter coordinates in indexes
letters_to_coordinates = {'a':0, 'b':1, 'c':2, 'd':3, "e":4, "f":5, "g":6, "h":7}
def king_neighbours(kings_coordinates):
    '''
        This function returns coordinates of all cell that neighbouring with the king's ceil
    :param kings_coordinates: tuple
        The coordinates of the king on chess table
    :return: list of tuples
        The list with the coordinates of the neighbours of the king
    '''
    i, j = kings_coordinates
    neighbours = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    to_del = []
    for n in neighbours:
        if -1 in n or 8 in n:
            to_del.append(n)
    for d in to_del:
        neighbours.remove(d)
    return neighbours
def manhattan_dist(a, b):
    '''
        Manhattan Distance
    :param a: tuple
        The coordinates of the cell A
    :param b: tuple
        The coordinates of the cell B
    :return: integer
        The manhattan distance
    '''
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def orintation(a, b):
    '''
        This function return the orientation of the kings move
    :param a: tuple
        The coordinates of the start cell
    :param b: tuple
        The coordinates of the finish cell
    :return: string
        String meaning the orientation of the move (R- right, L - left, U - Up, D - Down)
    '''
    o = ''
    if a[0] < b[0]:
        o += 'U'
    elif a[0] > b[0]:
        o+= 'D'
    if a[1] < b[1]:
        o+='R'
    elif a[1] > b[1]:
        o+= 'L'
    return o
i = int(input("Enter the row in which the king is:")) -1
j = letters_to_coordinates[input("Enter the column in which the king is:")]
king = (i, j)
i = int(input("Enter the row in which the target is:")) -1
j = letters_to_coordinates[input("Enter the column in which the target is:")]
target = (i, j)
number_or_moves = 0
moves = []
while True:
    # Getting all neighbours of the king's cell
    neighbours = king_neighbours(king)
    move_to = None
    # Getting the the Manhattan distance between the first neighbour and the target to compare latter
    min_dist = manhattan_dist(neighbours[0], target)
    # Finding the king's neighbour cell with the smallest Manhattan distance to the target
    for n in neighbours:
        if manhattan_dist(n, target) == 0:
            move_to = n
            break
        elif manhattan_dist(n, target) < min_dist:
            min_dist = manhattan_dist(n, target)
            move_to = n
    # Adding the move in the move's history
    moves.append(orintation(king, move_to))
    number_or_moves +=1
    # Changing the coordinates of the king anthe the move
    king = move_to
    if king == target:
        break
# Printing the result
print(number_or_moves)
for move in moves:
    print(move)