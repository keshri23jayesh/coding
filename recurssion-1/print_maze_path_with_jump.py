def print_maze_path(ans, i, j, max_i, max_j):

    if i == max_i and j == max_j:
        print(ans)
        return
    if i > max_i or j > max_j:
        return

    for jump in range(1, max_i- i + 1):
        print_maze_path('h'+str(jump) + ans, i + jump, j, max_i, max_j)
    for jump in range(1, max_j - j + 1):
        print_maze_path('v'+str(jump) + ans, i, j + jump, max_i, max_j)
    for jump in range(1, min(max_i- i + 1, max_j - j + 1)):
        print_maze_path('d'+str(jump) + ans, i + jump, j + jump, max_i, max_j)


print_maze_path('', 0, 0, 2, 2)