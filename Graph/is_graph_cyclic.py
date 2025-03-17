from queue import Queue

graph = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2, 4],
    [3, 5, 6],
    [4, 6, 2],
    [5, 4]
]

visited = set()

def find_cycle(node):
    que = Queue()
    que.put(node)
    while que:
        elem = que.get()
        if elem in visited:
            return True
        visited.add(elem)
        for vrtx in graph[elem]:
            if vrtx not in visited:
                que.put(vrtx)
    return False

print(find_cycle(0))