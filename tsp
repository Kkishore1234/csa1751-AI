from itertools import permutations


def travelling_salesman(graph, start):
    vertices = list(range(len(graph)))
    vertices.remove(start)
    min_path = float('inf')

    for perm in permutations(vertices):
        current_pathweight = 0
        k = start
        for j in perm:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][start]
        min_path = min(min_path, current_pathweight)

    return min_path


graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
start = 0
print("Minimum path:", travelling_salesman(graph, start))
