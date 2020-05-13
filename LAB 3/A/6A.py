inp = input("Enter the length of the sticks:")
a, b, c, d = tuple(inp.split())
a, b, c, d = int(a), int(b), int(c), int(d)
if (a < b+c and b < a+c and c < a+b) or (a < b+d and b < a+d and d < a+b) or (a < d+c and d < a+c and c < a+d) or (d < b+c and b < d+c and c < d+b):
    print("TRIANGLE")
elif (a == b+c or b == a+c or c == a+b) or (a == b+d or b == a+d or d == a+b) or (a == d+c or d == a+c or c == a+d) or (d == b+c or b == d+c or c == d+b):
    print("SEGMENT")
else:
    print("IMPOSSIBLE")