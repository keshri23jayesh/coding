

def get_stair_path(n):
    if n == 0:
        return ['']
    elif n < 0:
        return []

    path1 = get_stair_path(n-1)
    path2 = get_stair_path(n-2)
    path3 = get_stair_path(n-3)
    all_paths = []
    for path in path1:
        all_paths.append('1'+path)
    for path in path2:
        all_paths.append('2'+path)
    for path in path3:
        all_paths.append('3'+path)
    return all_paths


print(get_stair_path(3))
