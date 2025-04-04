# https://www.youtube.com/watch?v=dVT9JeUMMDE&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=26


l = 5
b = 2

dp_arr = [0] * (l + 1)

dp_arr[1] = 1
dp_arr[2] = 2


for i in range(3, len(dp_arr)):
    dp_arr[i] = dp_arr[i-2] + dp_arr[i-1]

print(dp_arr[-1])

