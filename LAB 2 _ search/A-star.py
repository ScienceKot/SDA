import numpy as np
import pandas as pd
def child_node(matrix, node, columns, was_before):
    for i in range(len(columns)):
        if columns[i] == node:
            return [columns[j] for j in range(len(columns)) if matrix[i][j] > 0 and columns[j] not in was_before]
def calc_path(path, columns, matrix):
    sum_path = 0
    if len(path) == 0:
        return 0
    for i in range(len(path)-1):
        index1 = columns.index(path[i])
        index2 = columns.index(path[i+1])
        sum_path+=matrix[index1][index2]
    return sum_path
distance_Buharest= {"Arad":366, "Bucharest":0, "Craiova":160, "Drobita":242, "Eforie":161,
                    "Fagaras":176, "Giurgiu":77, "Hirsova":151, "Iasi":226, "Lugoj":244,
                    "Mehedia":241, "Neamt":234, "Oradea":380, "Pitesti":100, "RM":193,
                    "Sibiu":253, "Timisoara":329, "Urziceni":80, "Vaslui":199, "Zerind":374}
def A_star(matrix, column, start, finish, dist):
    path = [start]
    explored = {start}
    while True:
        child_nodes = child_node(matrix, path[-1], column, explored)
        min_cost = calc_path(path, column, matrix) + dist[child_nodes[0]]
        to_expand = child_nodes[0]
        for child in child_nodes:
            if calc_path(path.copy(), column, matrix) + dist[child] < min_cost:
                min_cost = calc_path(path.copy(), column, matrix) + dist[child]
                to_expand = child
        explored.add(path[-1])
        path.append(to_expand)
        if finish in path:
            return path
df = pd.read_csv('map.csv')
X = df.values
best_path = A_star(X, list(df.columns), 'Oradea', 'Bucharest', distance_Buharest)
print(best_path)