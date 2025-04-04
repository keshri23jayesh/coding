# https://www.youtube.com/watch?v=BzTIOsC0xWM&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=7

matrix = [
    [2, 8, 4, 1, 6, 4, 2],
    [6, 0, 9, 5, 3, 8, 5],
    [1, 4, 3, 4, 0, 6, 5],
    [6, 4, 7, 2, 4, 6, 1],
    [1, 0, 3, 7, 1, 2, 7],
    [1, 5, 3, 2, 3, 0, 9],
    [2, 2, 5, 1, 9, 8, 2]
]

dp_arr = [[0]* len(matrix[0]) for _ in range(len(matrix))]
dp_arr[0][0] = matrix[0][0]

for i in range(1, len(matrix[0])):
    dp_arr[0][i] = dp_arr[0][i-1] + matrix[0][i]

for j in range(1, len(matrix)):
    dp_arr[j][0] = dp_arr[j-1][0] + matrix[j][0]

for i in range(1, len(dp_arr)):
    for j in range(1, len(dp_arr[0])):
        dp_arr[i][j] = matrix[i][j] + min(dp_arr[i-1][j], dp_arr[i][j-1])

print(dp_arr)