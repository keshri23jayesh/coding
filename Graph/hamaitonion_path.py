# https://www.youtube.com/watch?v=nUgp0RG57wQ&list=PL-Jc9J83PIiHfqDcLZMcO9SsUDY4S3a-v&index=9


graph = [
    [(1,10), (3,10)],
    [(0,10), (2,10)],
    [(1,10), (3,10), (2,5)],
    [(0,10), (2,10), (4,10)],
    [(3,10), (5,10), (6,10)],
    [(4,10), (6,10), (2,10)],
    [(5,10), (4,10)],
]


def hamltonian_path(src, orc, visited, psf):

    if len(visited) == (len(graph) - 1):
        print(psf)
        for node in graph[src]:
            if node[0] == src:
                type = '*'
            else:
                type = '.'
        print(type)
        print('-------')
        return

    visited.add(src)
    for node in graph[src]:
        vrtx, wgt = node
        if vrtx not in visited:
            hamltonian_path(vrtx, orc, visited, psf+" "+str(vrtx))
    visited.remove(src)


psf = "1"
src = 1
osrc = 1
visited = set()
hamltonian_path(src, osrc, visited, psf)