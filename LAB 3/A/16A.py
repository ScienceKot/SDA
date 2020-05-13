inp = input("Enter the sizes of the flag:")
n, m = tuple(inp.split())
n, m = int(n), int(m)
flag = []
f = open('16A.txt', 'r')
for line in f:
    flag.append(line[:-1])
f.close()
for line in flag:
    if len(set(line)) > 1:
        print("NO")
        quit()
for i in range(len(flag)-1):
    if set(flag[i]) == set(flag[i+1]):
        print('NO')
        quit()
print('YES')