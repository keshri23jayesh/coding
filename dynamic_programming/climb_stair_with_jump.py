def climbing_variable(n, dp):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if dp[n] != -1:
        return dp[n]

    ans_n = 0
    for i in range(n - 1, -1, -1):  # Corrected range to include 0
        ans_n += climbing_variable(i, dp)

    dp[n] = ans_n
    return ans_n


if __name__ == '__main__':
    n = 4
    dp = [-1] * (n + 1)  # Initialize dp with -1 for memoization
    print(climbing_variable(n, dp))
