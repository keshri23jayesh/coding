def flood_fill(i, j, ans, graph):
    if (i >= len(graph) or
            j >= len(graph[0]) or
            i < 0 or
            j < 0 or
            graph[i][j] == 1 or
            another_map[i][j] == 1):
        return
    if i == len(graph) - 1 and j == len(graph[0]) - 1:
        print(ans)
        return

    another_map[i][j] = 1
    flood_fill(i + 1, j, ans + 'd', graph)
    flood_fill(i - 1, j, ans + 't', graph)
    flood_fill(i, j + 1, ans + 'r', graph)
    flood_fill(i, j - 1, ans + 'l', graph)
    another_map[i][j] = 0


graph = [[0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 1, 1],
         [1, 0, 1, 1, 0, 1, 1],
         [1, 0, 0, 0, 0, 0, 0]]

another_map = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0], ]

flood_fill(0, 0, '', graph)
