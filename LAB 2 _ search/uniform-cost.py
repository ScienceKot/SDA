import numpy as np
import pandas as pd
def child_node(matrix, node, columns, was_before):
    for i in range(len(columns)):
        if columns[i] == node:
            return [columns[j] for j in range(len(columns)) if matrix[i][j] > 0 and columns[j] not in was_before]
def calc_path(path, columns, matrix):
    sum_path = 0
    for i in range(len(path)-1):
        index1 = columns.index(path[i])
        index2 = columns.index(path[i+1])
        sum_path+=matrix[index1][index2]
    return sum_path
def uniform_cost(matrix, column, start, finish):
    frontier = [[start]]
    explored = {start}
    frontier_plus = []
    while True:
        if len(explored) == len(column):
            if len(frontier_plus) > 0:
                finish_index = frontier_plus[0].index(finish)
                return frontier_plus[0][:finish_index+1]
            else:
                return "failure"
        to_pop = len(frontier)
        for i in range(len(frontier)):
            child_nodes = child_node(matrix, frontier[i][-1], column, explored)
            for child in child_nodes:
                frontier.append(frontier[i].copy()+[child])
            explored.add(frontier[i][-1])
        to_delete = []
        for i in range(to_pop):
            to_delete.append(frontier[i])
        for front in to_delete:
            frontier.remove(front)
        for i in range(len(frontier)):
            if finish in frontier[i]:
                frontier_plus.append(frontier[i].copy())
        for i in range(len(frontier_plus)):
            for j in range(len(frontier_plus)-1):
                if calc_path(frontier_plus[j], column, matrix) > calc_path(frontier_plus[j+1], column, matrix):
                    frontier_plus[j], frontier_plus[j+1] = frontier_plus[j+1].copy(), frontier_plus[j].copy()
        for i in range(len(frontier)):
            for j in range(len(frontier)-1):
                if calc_path(frontier[j], column, matrix) > calc_path(frontier[j+1], column, matrix):
                    frontier[j], frontier[j+1] = frontier[j+1].copy(), frontier[j].copy()
df = pd.read_csv('map.csv')
X = df.values
best_path = uniform_cost(X, list(df.columns), 'Vaslui', 'Arad')
print(best_path)