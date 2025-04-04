# https://www.youtube.com/watch?v=bUSaenttI24&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=16

profit = [15, 14, 10, 45, 30]
weight = [2, 5, 1, 3, 4]
max_weight = 7

dp_arr = [[0] * (max_weight + 1) for _ in range(len(weight)+1)]


for row in range(len(dp_arr)):
    for column in range(len(dp_arr[0])):
        if row == 0 or column == 0:
            dp_arr[row][column] = 0
        else:
            if column < weight[row-1]:
                dp_arr[row][column] = dp_arr[row-1][column]
            else:
                dp_arr[row][column] = max(dp_arr[row-1][column],
                                          profit[row-1] + dp_arr[row-1][column-weight[row-1]])


for row in dp_arr:
    print(row)

print(dp_arr[-1][-1])