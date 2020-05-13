inp = input("Enter the number of houses and the side of the new house")
n, t = tuple(inp.split())
n, t = int(n), int(t)
ways = 0
houses = []
for i in range(n):
    inp = input("Enter the origin of the house and the length of the side:")
    x, a = tuple(inp.split())
    houses.append([int(x), int(a)])
mini = houses[0][0]
min_interval = houses[0][1]/2
maxi = houses[0][0]
max_interval = houses[0][1]/2
for h in houses:
    if mini > h[0]:
        mini = h[0]
        min_interval = h[1]/2
    if maxi < h[0]:
        maxi = h[0]
        max_interval = h[1]/2
intervals = []
intervals.append(('-inf', mini - min_interval))
intervals.append((maxi + max_interval, '+inf'))
for i in range(len(houses)):
    for j in range(len(houses)-1):
        if houses[j][0] > houses[j+1][0]:
            houses[j], houses[j+1] = houses[j+1].copy(), houses[j].copy()
for i in range(len(houses)-1):
    if mini in houses[i]:
        intervals.append((houses[i][0] + houses[i][1]/2, houses[i+1][0] - houses[i+1][1]/2))
    elif maxi in houses:
        intervals.append((houses[i-1][0] + houses[i-1][1]/2, houses[i][0] - houses[i][1]/2))
    else:
        intervals.append((houses[i][0] + houses[i][1]/2, houses[i+1][0] - houses[i+1][1]/2))
        intervals.append((houses[i-1][0] + houses[i-1][0]/2, houses[i][0] - houses[i][1]/2))
intervals = list(set(intervals))
for interval in intervals:
    if "+inf" in interval or '-inf' in interval:
        ways +=1
    elif interval[1] - interval[0] > t:
        ways +=2
    elif interval[1] - interval[0] == t:
        ways +=1
print(ways)
