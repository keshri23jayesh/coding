# https://www.youtube.com/watch?v=kh48JLieeW8&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=23
            #  r,g,b
paint_cost = [[1,5,7],
              [5,8,4],
              [3,2,9],
              [1,2,4]]

dp_arr = [[10000000] * len(paint_cost[0]) for _ in range(len(paint_cost))]

i = 0
for elem in paint_cost[0]:
    dp_arr[0][i] = elem
    i += 1

for i in range(1, len(paint_cost)):
    for j in range(0, len(dp_arr[0])):
        for k in range(0, len(dp_arr[0])):
            if j == k:
                continue
            dp_arr[i][j] = min(dp_arr[i][j],
                               dp_arr[i-1][k]+paint_cost[i][j])

for row in dp_arr:
    print(row)