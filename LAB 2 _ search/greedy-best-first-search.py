import numpy as np
import pandas as pd
def child_node(matrix, node, columns, was_before):
    for i in range(len(columns)):
        if columns[i] == node:
            return [columns[j] for j in range(len(columns)) if matrix[i][j] > 0 and columns[j] not in was_before]
distance_Buharest= {"Arad":366, "Bucharest":0, "Craiova":160, "Drobita":242, "Eforie":161,
                    "Fagaras":176, "Giurgiu":77, "Hirsova":151, "Iasi":226, "Lugoj":244,
                    "Mehedia":241, "Neamt":234, "Oradea":380, "Pitesti":100, "RM":193,
                    "Sibiu":253, "Timisoara":329, "Urziceni":80, "Vaslui":199, "Zerind":374}
def greedy_best_first_search(matrix, columns, start, finish, dist):
    path = [start]
    explored = {start}
    while True:
        child_nodes = child_node(matrix, path[-1], columns, explored)
        min_dist = dist[child_nodes[0]]
        best_child = None
        for child in child_nodes:
            if dist[child] <= min_dist:
                best_child = child
        path.append(best_child)
        explored.add(best_child)
        if finish in path:
            return path
df = pd.read_csv("map.csv")
X = df.values
best_path = greedy_best_first_search(X, list(df.columns), "Timisoara", "Bucharest", distance_Buharest)
print(best_path)