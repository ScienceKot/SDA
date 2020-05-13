import pandas as pd
import numpy as np
def child_node(matrix, node, columns, was_before=None):
    for i in range(len(columns)):
        if columns[i] == node:
            return [columns[j] for j in range(len(columns)) if matrix[i][j] > 0 and columns[j] not in was_before]
def depth_first(matrix, column, node_to_extend, finish, path=[], explored=set()):
    if node_to_extend not in explored:
        explored.add(node_to_extend)
    if len(path) == 0:
        path = [node_to_extend]
    if len(path) == 1:
        child_nodes = child_node(matrix, path[-1], column, explored.copy())
    else:
        new_explored = explored.copy()
        new_explored.add(path[-2])
        child_nodes = child_node(matrix, path[-1], column, new_explored)
    if len(child_nodes) ==0:
        return
    else:
        for child in child_nodes:
            new_path = path.copy() + [child]
            if finish in new_path:
                return new_path
            return depth_first(matrix, column, child, finish, new_path, explored.copy())
df = pd.read_csv('map.csv')
X = df.values
best_path = depth_first(X, list(df.columns), 'Neamt', 'RM')
print(best_path)