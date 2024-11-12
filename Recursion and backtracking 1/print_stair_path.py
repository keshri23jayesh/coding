def print_stair_path(path, n):
    if n == 0:
        print(path)
        return
    if n < 0:
        return
    print_stair_path('1' + path, n - 1)
    print_stair_path('2' + path, n - 2)
    print_stair_path('3' + path, n - 3)


print_stair_path('', 3)
