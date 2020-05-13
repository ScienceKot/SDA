import numpy as np
import pandas as pd
import random
def child_node(matrix, node, columns, was_before):
    for i in range(len(columns)):
        if columns[i] == node:
            return [columns[j] for j in range(len(columns)) if matrix[i][j] > 0 and columns[j] not in was_before]
def bidirectional_search(matrix, columns, start, finish):
    queue_start = [[start]]
    was_before_start = {start}
    queue_finish = [[finish]]
    was_before_finish = {finish}
    while True:
        to_pop_start = len(queue_start)
        was_start = []
        for i in range(len(queue_start)):
            child_nodes = child_node(matrix, queue_start[i][-1], columns, was_before_start)
            was_start.append(queue_start[i][-1])
            for child in child_nodes:
                to_append = queue_start[i].copy()
                to_append.append(child)
                queue_start.append(to_append)
        was_before_start.update(set(was_start))
        to_remove = []
        for i in range(to_pop_start):
            to_remove.append(queue_start[i])
        for i in to_remove:
            queue_start.remove(i)
        # from finish
        to_pop_finish = len(queue_finish)
        was_finish = []
        for i in range(len(queue_finish)):
            child_nodes = child_node(matrix, queue_finish[i][-1], columns, was_before_finish)
            was_finish.append(queue_finish[i][-1])
            for child in child_nodes:
                to_append = queue_finish[i].copy()
                to_append.append(child)
                queue_finish.append(to_append)
        was_before_finish.update(set(was_finish))
        to_remove = []
        for i in range(to_pop_finish):
            to_remove.append(queue_finish[i])
        for i in to_remove:
            queue_finish.remove(i)
        start_total, finish_total = set(), set()
        for q in queue_start:
            start_total.update(set(q))
        for q in queue_finish:
            finish_total.update(set(q))
        same_values = start_total.intersection(finish_total)
        first_part, second_part = None, None
        if len(same_values) !=0:
            point = random.sample(same_values, 1)[0]
            for i in range(len(queue_start)):
                if point in queue_start[i]:
                    first_part = queue_start[i][:queue_start[i].index(point)+1]
            for i in range(len(queue_finish)):
                if point in queue_finish[i]:
                    second_part = queue_finish[i]
            if first_part != None and second_part != None:
                return first_part + list(reversed(second_part))[1:]
df = pd.read_csv('map.csv')
X = df.values
best_path = bidirectional_search(X, list(df.columns), 'Vaslui', 'Sibiu')
print(best_path)