# https://www.youtube.com/watch?v=_c_R-uIi-zU&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=27

# solve again

length = 5
breadth = 4

dp_arr = [0] * (length + 1)

for i in range(1, length+1):
    if i < breadth:
        dp_arr[i] = 1
    elif i == breadth:
        dp_arr[i] = 2
    else:
        dp_arr[i] = dp_arr[i-1] + dp_arr[i-breadth]

print(dp_arr)