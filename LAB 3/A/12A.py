# To write this problem I used the theory from this wikipedia page : https://en.wikipedia.org/wiki/Centrosymmetric_matrix
def check_centrosymetry(mat):
    chechpoints = 0
    n = len(mat)
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == mat[n-i-1][n-j-1]:
                chechpoints +=1
    if chechpoints == 9:
        return True
    else:
        return False
matrix = []
f = open('12A.txt', 'r')
for line in f:
    matrix.append(list(line[:-1]))
if check_centrosymetry(matrix):
    print('YES')
else:
    print('NO')