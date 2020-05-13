d, sumTime = tuple(input("Enter the number of days and the sum of hours pent of learning:").split())
d, sumTime = int(d), int(sumTime)
intervals = []
for i in range(d):
    minTime, maxTime = tuple(input('Enter the limits of time for this time:').split())
    intervals.append((int(minTime), int(maxTime)))
sumi = 0
for i in intervals:
    sumi += i[1]
if sumi >= sumTime:
    print('YES')
    for i in intervals:
        if i[1] - i[0] == i[1]:
            print(i[1], end=' ')
        else:
            print(sumTime, end=' ')
        sumTime -= i[1] - i[0]
else:
    print('NO')