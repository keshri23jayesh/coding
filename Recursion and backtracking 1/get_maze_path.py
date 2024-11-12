def get_maze_path(i, j, max_i, max_j):
    if i == max_i and j == max_j:
        return ['']

    ans = []
    if i < max_i:
        path1 = get_maze_path(i+1, j, max_i, max_j)
        for path in path1:
            ans.append('h' + path)

    if j < max_j:
        path2 = get_maze_path(i, j+1, max_i, max_j)
        for path in path2:
            ans.append('v' + path)

    return ans


print(get_maze_path(0, 0, 2, 2))
