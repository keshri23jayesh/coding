graph = [
    [(1,10), (3,10)],
    [(0,10), (2,10)],
    [(1,10), (3,10)],
    [(0,10), (2,10), (4,10)],
    [(3,10), (5,10), (6,10)],
    [(4,10), (6,10)],
    [(5,10), (4,10)],
]
visited = set()
def print_all_src_dst(src, dest, psf):
    if src == dest:
        print(psf)
        return
    visited.add(src)
    for nbr in graph[src]:
        node, edge = nbr
        if node not in visited:
            print_all_src_dst(node, dest, psf +" "+ str(node))
    visited.remove(src)

print_all_src_dst(0, 5, "0")