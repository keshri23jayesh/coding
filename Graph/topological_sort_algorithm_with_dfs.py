
graph = [
    [1, 3],
    [2],
    [3],
    [],
    [3, 5, 6],
    [6],
    []
]


visited = set()
stack = list()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for elem in graph[node]:
        if elem not in visited:
            dfs(elem)
    stack.append(node)

for node, edges in enumerate(graph):
    dfs(node)

print(stack)



