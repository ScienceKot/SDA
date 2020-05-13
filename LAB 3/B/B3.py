inp = input("Enter the number  of waterborne vehicles and the truck body volume of the lorry in cubic metres:")
n, v = tuple(inp.split())
n, v = int(n), int(v)
maxi =0
max_index = 0
for i in range(n):
    t, p = tuple(input("Enter the vehicle type (1 = kayak, 2 = catamaran) and it's carrying capacity:").split())
    t, p = int(t), int(p)
    if p > maxi:
        maxi = p
        max_index = i
print(maxi)
print(max_index+1)