

def print_maze_path(ans, i, j, max_i, max_j):

    if i == max_i and j == max_j:
        print(ans)
        return
    if i > max_i or j > max_j:
        return

    print_maze_path('h'+ans, i+1, j, max_i, max_j)
    print_maze_path('v'+ans, i, j+1, max_i, max_j)


print_maze_path('', 0, 0, 3, 3)