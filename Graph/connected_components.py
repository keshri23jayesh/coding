graph = [
    [(1,10)],
    [(0,10)],
    [(3,10)],
    [(2,10)],
    [(5,10), (6,10)],
    [(4,10), (6,10)],
    [(5,10), (4,10)],
]

visited = set()

def dfs(node):
    stack = list()
    stack.append(node)
    cc = False
    while stack:
        node = stack.pop()
        for nbr in graph[node]:
            vertx, edge = nbr
            if vertx not in visited:
                cc = True
                visited.add(vertx)
                stack.append(vertx)
    return cc



def connected_component(graph):
    cc = 0
    for idx, node in enumerate(graph):
        if idx not in visited and dfs(idx):
            cc += 1
    print(cc)

connected_component(graph)