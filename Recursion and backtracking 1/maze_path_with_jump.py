def get_maze_path_with_jump(i, j, max_i, max_j):
    if i == max_i and j == max_j:
        return ['']

    ans = []

    for jump_size in range(1, max_i-i+1):
        hpaths = get_maze_path_with_jump(i+jump_size, j, max_i, max_j)
        for path in hpaths:
            ans.append('h'+str(jump_size)+path)

    for jump_size in range(1, max_j-j+1):
        vpaths = get_maze_path_with_jump(i, j+jump_size, max_i, max_j)
        for path in vpaths:
            ans.append('v' + str(jump_size) + path)

    for jump_size in range(1, min(max_i-i+1, max_j-j+1)):
        dpaths = get_maze_path_with_jump(i+jump_size, j+jump_size, max_i, max_j)
        for path in dpaths:
            ans.append('d' + str(jump_size) + path)

    return ans


print(get_maze_path_with_jump(0, 0, 2, 2))
