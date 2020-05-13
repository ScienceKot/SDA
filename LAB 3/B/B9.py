def euclidean_dist(first, second):
    return (first[0] - second[0])**2 + (first[1] - second[1])**2
n, vb, vs = tuple(input("Enter the number of bus stantions, speed of the bus and the speed of the student:").split())
n, vb, vs = int(n), int(vb), int(vs)
bus_stantions = input("Enter the x coordinates of bus stntions:").split()
bus_stantions = [int(x) for x in bus_stantions]
uni= tuple(input("Enter the coordinates of University:").split())
uni = tuple([int(uni[0]), int(uni[1])])
min_dist = 0 + euclidean_dist((0, 0), uni)
stantion_index =0
for stantion in bus_stantions:
    if min_dist > stantion + euclidean_dist((stantion, 0), uni):
        min_dist = stantion + euclidean_dist((stantion, 0), uni)
        stantion_index = bus_stantions.index(stantion)
print(stantion_index+1)