# https://www.youtube.com/watch?v=A6mOASLl2Dg&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=2

n = 3
dp = [0] * 4

def climbing(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    if dp[n]:
        return dp[n]

    n1 = climbing(n-1)
    n2 = climbing(n-2)
    n3 = climbing(n-3)
    ans = n1 + n2 + n3
    dp[n] = ans
    return ans


print(climbing(3))



