"""
dfs.py
"""

def dfs(graph,start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)

            stack.extend(graph[vertex] - visited)
    return visited