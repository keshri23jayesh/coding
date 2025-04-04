# https://www.youtube.com/watch?v=SHDu0Ufjyk8&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=28

n = 4
dp_arr = [0] * (n+1)

dp_arr[0] = 0
dp_arr[1] = 1
dp_arr[2] = 2


for i in range(3, len(dp_arr)):
    dp_arr[i] = dp_arr[i-1] + (i-1) * dp_arr[i-2]

print(dp_arr)





