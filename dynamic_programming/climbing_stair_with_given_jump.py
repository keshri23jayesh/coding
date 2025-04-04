
def climbing_variable(n, jump_array):
    dp = [0] * (n + 1)  # Initialize dp with -1
    dp[-1] = 1 # climbing form 0 to n
    for i in range(n-1, -1, -1):
        for j in range(1, jump_array[i]+1):
            if i+j < len(dp):
                dp[i] += dp[i+j]

    print(dp)

if __name__ == '__main__':
    n = 6  # Number of steps
    jump_array = [3, 3, 0, 2, 2, 3]  # Jump range at each step
    climbing_variable(n, jump_array)