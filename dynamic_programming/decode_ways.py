# https://www.youtube.com/watch?v=jFZmBQ569So&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=20

arr = ['0','3','1','0','1','1']
n = len(arr)
dp = [0] * (n)

dp[0] = 1
dp[1] = 2

def is_valid_num(num1, num2):
    if num1 == '0':
        return False
    if 0 < int(num1 + num2) < 27:
        return True
    return False

for i in range(2, n):
    if arr[i] == '0':
        if is_valid_num(arr[i-1], arr[i]):
            dp[i] = dp[i-2]
    else:
        dp[i] = dp[i-1]
        if is_valid_num(arr[i-1], arr[i]):
            dp[i] += dp[i - 2]

print(dp)