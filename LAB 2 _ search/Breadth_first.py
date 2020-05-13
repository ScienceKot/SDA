import pandas as pd
import numpy as np
def child_node(matrix, node, columns, was_before):
    for i in range(len(columns)):
        if columns[i] == node:
            return [columns[j] for j in range(len(columns)) if matrix[i][j] > 0 and columns[j] not in was_before]
def breadth_firts(matrix, columns, start, finish):
    queue = [[start]]
    was_before = {start}
    while True:
        to_pop = len(queue)
        was = []
        for i in range(len(queue)):
            child_nodes = child_node(matrix, queue[i][-1], columns, was_before)
            was.append(queue[i][-1])
            for child in child_nodes:
                to_append = queue[i].copy()
                to_append.append(child)
                queue.append(to_append)
                if child == finish:
                    return queue[-1]
        was_before.update(set(was))
        to_remove = []
        for i in range(to_pop):
            to_remove.append(queue[i])
        for i in to_remove:
            queue.remove(i)
        print(queue)
df = pd.read_csv('map.csv')
X = df.values
path = breadth_firts(X, list(df.columns), 'Oradea', "Craiova")
print(path)