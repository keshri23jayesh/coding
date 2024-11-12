# https://www.youtube.com/watch?v=lNwXq3Ki32I&list=PL3UlF_QlQi8xyUGvQO0pHnX64YCt76j2E&index=6

def get_gold(i, j, bag, matrix, visited):
    if i < 0 or j < 0 or i > len(matrix)-1 or j > len(matrix[0])-1 or visited[i][j] != 0 or matrix[i][j] == 0:
        return

    visited[i][j] = 1
    bag.append(matrix[i][j])
    get_gold(i + 1, j, bag, matrix, visited)
    get_gold(i - 1, j, bag, matrix, visited)
    get_gold(i, j + 1, bag, matrix, visited)
    get_gold(i, j - 1, bag, matrix, visited)


matrix = [
    [10, 0, 100, 200, 0, 8, 0],
    [20, 0, 0, 0, 0, 6, 0],
    [30, 0, 0, 9, 12, 3, 4],
    [4, 0, 2, 5, 8, 3, 11],
    [0, 0, 0, 0, 0, 9, 0],
    [5, 6, 7, 0, 7, 4, 2],
    [8, 9, 10, 0, 1, 10, 8]
]

visited = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

max_sum = -1
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] != 0 and visited[i][j] == 0:
            bag = []
            get_gold(i, j, bag, matrix, visited)
            arr_sum = sum(bag)
            max_sum = max(max_sum, arr_sum)

print(max_sum)
