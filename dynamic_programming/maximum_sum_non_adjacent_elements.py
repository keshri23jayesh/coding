# https://www.youtube.com/watch?v=VT4bZV24QNo&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=22

arr = [5,10,10,100,5,6]
# arr = [5,4,10,100,5,6]

dp_arr = [0] * len(arr)
dp_arr[0] = arr[0]
dp_arr[1] = max(arr[0], arr[1])


for i in range(2, len(arr)):
    if dp_arr[i-1] > arr[i] + dp_arr[i-2]:
        dp_arr[i] = dp_arr[i-1]
    else:
        dp_arr[i] = dp_arr[i-2] + arr[i]

print(dp_arr)