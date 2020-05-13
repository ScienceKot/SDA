def choose(coordinates, matrix):
    down = tuple([coordinates[0]+1, coordinates[1]])
    if down[0] == len(matrix):
        return 'R'
    if down[1] == len(matrix):
        return 'D'
    if matrix[down[0]][down[1]] !=0:
        return 'D'
    else:
        return 'R'
n = int(input("Enter the size of the matrix:"))
matrix = []
for i in range(n):
    print("Enter {} number of the row number {}:".format(n, i+1), end='')
    inp = input()
    row = inp.split()
    row = [int(x) for x in row]
    matrix.append(row)
start = tuple([0, 0])
solution = ''
zeros = 0
while True:
    if start == tuple([n-1, n-1]):
        break
    if matrix[start[0]][start[1]] == 0:
        zeros +=1
    step = choose(start, matrix)
    if step == 'D':
        start = tuple([start[0]+1, start[1]])
    else:
        start = tuple([start[0], start[1]+1])
    solution+=step
print(zeros)
print(solution)