# https://www.youtube.com/watch?v=sD0lLYlGCJE&list=PL-Jc9J83PIiHfqDcLZMcO9SsUDY4S3a-v&index=15
import heapq

graph = [
    [(1, 10), (3, 20)],  # Node 0 is connected to Node 1 (weight 10) and Node 3 (weight 20)
    [(0, 10), (2, 15)],  # Node 1 is connected to Node 0 (weight 10) and Node 2 (weight 15)
    [(1, 15), (3, 25)],  # Node 2 is connected to Node 1 (weight 15) and Node 3 (weight 25)
    [(0, 20), (2, 25), (4, 30)],  # Node 3 is connected to Nodes 0, 2, and 4
    [(3, 30), (5, 35), (6, 40)],  # Node 4 is connected to Nodes 3, 5, and 6
    [(4, 35), (6, 45)],  # Node 5 is connected to Nodes 4 and 6
    [(5, 45), (4, 40)],  # Node 6 is connected to Nodes 5 and 4
]

pq = []
heapq.heappush(pq, (0,0))
visited = set()

while pq:
    # remove
    node, dis = heapq.heappop(pq)
    if node in visited:
        continue
    #mark
    visited.add(node)

    # work
    print(node, dis)

    # add neighbour
    for nbr, weight in graph[node]:
        if nbr not in visited:
            heapq.heappush(pq,(nbr, dis + weight))
