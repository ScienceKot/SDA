inp = input("Enter the sizes of the drawing:")
n, m = tuple(inp.split())
n, m = int(n), int(m)
matrix = []
f = open('14A.txt', 'r')
for line in f:
    matrix.append(list(line[:-1]))
to_del = []
for i in range(n):
    if set(matrix[i]) == set(['.']):
        to_del.append(i)
for i in to_del:
    matrix.pop(i)
matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
to_del = []
for i in range(len(matrix)):
    if set(matrix[i]) == set(['.']):
        to_del.append(i)
for i in to_del[::-1]:
    matrix.pop(i)
matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
for row in matrix:
    print(row)