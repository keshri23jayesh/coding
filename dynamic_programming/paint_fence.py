# https://www.youtube.com/watch?v=ju8vrEAsa3Q&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=25


no_of_fence = 5
colors = 3


dp_arr = [[0]* (no_of_fence + 1) for i in range(2)]

dp_arr[0][1] = colors
dp_arr[1][1] = colors * (colors - 1)

for col in range(2, len(dp_arr[0])):
    if col == 0:
        continue
    dp_arr[0][col] = dp_arr[1][col-1]
    dp_arr[1][col] = dp_arr[0][col-1] + (dp_arr[1][col-1]) * 2

print(dp_arr)