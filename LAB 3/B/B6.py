def desk_neighbours(president_desk, matrix):
    i, j = president_desk
    neighbours = [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]
    to_del = []
    for n in neighbours:
        if -1 in n or len(matrix) == n[0] or len(matrix[0]) == n[1]:
            to_del.append(n)
    for d in to_del:
        neighbours.remove(d)
    return neighbours
n, m, c = tuple(input("Enter the length, width, and the leter that will mean the President's desk:").split())
n, m, c = int(n), int(m), c
room = []
f = open('B6.txt', 'r')
for line in f:
    room.append(list(line[:-1]))
presidets_desk = []
for i in range(n):
    for j in range(m):
        if room[i][j] == c:
            presidets_desk.append((i, j))
neighbours = []
for coordinates in presidets_desk:
    n = desk_neighbours(coordinates, room)
    for value in n:
        neighbours.append(room[value[0]][value[1]])
neighbours = set(neighbours)
if c in neighbours:
    neighbours.remove(c)
neighbours.remove('.')
print(len(neighbours))
