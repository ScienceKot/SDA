def dist(x1, x2, y1, y2):
    return (x1-x2)**2 + (y1 - y2)**2
def check(arr):
    for i in range(len(arr)):
        arr[i] -=1
        d1 = dist(arr[0], arr[1], arr[2], arr[3])
        d2 = dist(arr[0], arr[1], arr[4], arr[5])
        d3 = dist(arr[2], arr[3], arr[4], arr[5])
        arr[i] +=1
        if d1 ==0 or d2 == 0 or d3 == 0:
            continue
        if d1 == d2 + d3 or d2 == d1 + d3 or d3 == d1 + d2:
            return True
    for i in range(len(arr)):
        arr[i] += 1
        d1 = dist(arr[0], arr[1], arr[2], arr[3])
        d2 = dist(arr[0], arr[1], arr[4], arr[5])
        d3 = dist(arr[2], arr[3], arr[4], arr[5])
        arr[i] -= 1
        if d1 == 0 or d2 == 0 or d3 == 0:
            continue
        if d1 == d2 + d3 or d2 == d1 + d3 or d3 == d1 + d2:
            return True
    return False
inp = input("Enter the cardezian coordinates of the points:")
arr = inp.split()
arr = [int(x) for x in arr]
d1 = dist(arr[0], arr[1], arr[2], arr[3])
d2 = dist(arr[0], arr[1], arr[4], arr[5])
d3 = dist(arr[2], arr[3], arr[4], arr[5])
if d1 == d2 + d3 or d2 == d1 + d3 or d3 == d1 + d2:
    print("RIGHT")
elif check(arr):
    print("ALMOST")
else:
    print("NEITHER")