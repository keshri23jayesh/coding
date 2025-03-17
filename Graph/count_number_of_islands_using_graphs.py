island_map = [
    [0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
]

def visited_island(i, j):
    if ((i < 0 or j < 0 or i > (len(island_map) - 1)
            or j > (len(island_map[0]) - 1)
            or island_map[i][j] == 'V')
            or island_map[i][j] == 1):
        return

    if island_map[i][j] == 0:
        island_map[i][j] = 'V'

    visited_island(i+1, j)
    visited_island(i-1, j)
    visited_island(i, j+1)
    visited_island(i, j-1)

def count_island(island_map):
    num_island = 0
    for i in range(0, len(island_map)):
        for j in range(0, len(island_map[0])):
            if island_map[i][j] == 0 and island_map[i][j] != 'V':
                visited_island(i, j)
                num_island += 1
    print(num_island)

count_island(island_map)