from collections import deque
def bfs(graph,start):
    queue=deque([start])
    visited=set([start])
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
graph= {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
bfs(graph,'A')
