class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)  # For an undirected graph

    def display(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])

"""
# Example usage
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.display()
"""
graph = [[(1,10), (3,10)],
         [(0,10), (2,10)],
         [(1,10), (3,10)],
         [(0,10), (2,10), (4,10)],
         [(3,10), (5,10), (6,10)],
         [(4,10), (6,10)]]

visited = set()


def has_path(graph, src, dest):
    if src == dest:
        return True

    for nbr in graph[src]:
        node, dist = nbr
        if node not in visited:
            visited.add(node)
            has_dest_path = has_path(graph, node, dest)
            if has_dest_path:
                return True
    return False

print(has_path(graph, 2, 5))