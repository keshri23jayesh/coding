# https://www.youtube.com/watch?v=5KdvH15NJjc&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=8

matrix = [
    [0, 1, 4, 2, 8, 2],
    [4, 3, 6, 5, 0, 4],
    [1, 2, 4, 1, 4, 6],
    [2, 0, 7, 3, 2, 2],
    [3, 1, 5, 9, 2, 4],
    [2, 7, 0, 8, 5, 1]
]

dp_arr = [[0]* len(matrix[0]) for _ in range(len(matrix))]
dp_arr[0][0] = matrix[0][0]

for j in range(0, len(matrix)):
    dp_arr[j][-1] = matrix[j][-1]

for j in range(len(matrix[0])-2, -1, -1):
    for i in range(len(matrix)):
        if i == 0:
            dp_arr[i][j] = matrix[i][j] + max(dp_arr[i][j+1], dp_arr[i+1][j+1])
        elif i == len(matrix)-1:
            dp_arr[i][j] = matrix[i][j] + max(dp_arr[i][j+1], dp_arr[i-1][j+1])
        else:
            dp_arr[i][j] = matrix[i][j] + max(dp_arr[i][j+1], dp_arr[i-1][j+1], dp_arr[i+1][j+1])

print(dp_arr)






