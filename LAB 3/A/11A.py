import random
def is_encreassing(seq):
    point = 0
    for i in range(len(seq)-1):
        if seq[i] < seq[i+1]:
            point+=1
    if point == len(seq)-1:
        return True
    else:
        return False
inp = input("Enter the length of sequence and the diference:")
n, d = tuple(inp.split())
n, d = int(n), int(d)
inp = input("Enter the sequence:")
seq = inp.split()
seq = [int(x) for x in seq]
moves = 0
while not is_encreassing(seq):
    i = random.randint(0, len(seq)-1)
    seq[i] +=d
    moves +=1
print(moves)