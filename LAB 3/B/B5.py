from math import floor, ceil
strings = []
while True:
    inp = input()
    if inp == 'stop':
        break
    else:
        strings.append(inp)
max_length = 0
for string in strings:
    if len(string) > max_length:
        max_length = len(string)
print((max_length+2)*'*')
for s in strings:
    print('*', end='')
    print(floor((max_length - len(s))/2)*' ',end='')
    print(s, end='')
    print(ceil((max_length - len(s))/2)*' ',end='')
    print('*')
print((max_length+2)*'*')