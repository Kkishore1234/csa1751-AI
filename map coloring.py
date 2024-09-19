def is_safe(node, color, graph, colors):
    for neighbor in graph[node]:
        if color == colors[neighbor]:
            return False
    return True

def map_coloring(graph, colors_available, colors, node):
    if node == len(graph):
        return True

    for color in colors_available:
        if is_safe(node, color, graph, colors):
            colors[node] = color
            if map_coloring(graph, colors_available, colors, node + 1):
                return True
            colors[node] = None
    return False

def solve_map_coloring(graph, colors_available):
    colors = [None] * len(graph)
    if map_coloring(graph, colors_available, colors, 0):
        return colors
    else:
        return None

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

colors_available = ['Red', 'Green', 'Blue']
solution = solve_map_coloring(graph, colors_available)
print("Solution:", solution)
