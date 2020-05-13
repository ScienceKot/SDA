inp = input("Enter the data:")
n, P1, P2, P3, T1, T2 = tuple(inp.split())
n, P1, P2, P3, T1, T2 = int(n), int(P1), int(P2), int(P3), int(T1), int(T2)
work_intervals = []
total_time = 0
for i in range(n):
    inp = input("Enter the work time range:")
    l, r = tuple(inp.split())
    work_intervals.append(tuple([int(l), int(r)]))
if n == 1:
    total_time = (work_intervals[0][1] - work_intervals[0][0]) * P1
i = 0
while True:
    total_time += (work_intervals[i][1] - work_intervals[i][0]) * P1
    if i == n-1:
        break
    print(i)
    print(total_time)
    if work_intervals[i+1][0] - work_intervals[i][1] > T1:
        total_time += T1 * P1
        last_time = work_intervals[i+1][0] - work_intervals[i][1] - T1
    else:
        total_time += P1 * (work_intervals[i+1][0] - work_intervals[i][1])
        last_time = 0
    print(total_time)
    if last_time > 0:
        if last_time > T2:
            total_time+=P2*T2
            last_time -= T2
        else:
            total_time += P2 * last_time
            last_time = 0
    print(total_time)
    total_time +=last_time * P3
    i+=1
print(total_time)
