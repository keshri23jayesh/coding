# https://www.youtube.com/watch?v=jgps7MXtKRQ&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=17

profit_arr = [10,15,45,30,14]
weight_arr = [1,2,3,4,5]

target = 7

dp_arr = [0] * (target + 1)

for index, cur_score in enumerate(dp_arr):
    if index == 0:
        continue
    for weight_idx, weight in enumerate(weight_arr):
        if weight > index:
            continue
        dp_arr[index] = max(dp_arr[index],
                        dp_arr[index-weight] + profit_arr[weight_idx])

print(dp_arr)
