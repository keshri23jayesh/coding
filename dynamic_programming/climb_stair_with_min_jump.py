
def climbing_variable(n, jump_array):
    dp = [None] * (n + 1)  # Initialize dp with -1
    dp[-1] = 0 # no move if we are not runnuing => meaning  10 se 10 main 0 move
    for i in range(n-1, -1, -1): # meaning of the filling from last to zero -> cause we have to calcualte dp[0]
        for j in range(1, jump_array[i]+1):
            if jump_array[i] > 0:
                min_val = 100000
                if i + j < len(dp):
                    if dp[i+j] is not None:
                        min_val = min(dp[i+j], min_val)
                if min_val == 100000:
                    dp[i] = None
                else:
                    dp[i] = min_val + 1
    print(dp)

if __name__ == '__main__':
    n = 10  # Number of steps
    jump_array = [3, 2, 4, 2, 0, 2, 3, 1, 2, 2]  # Jump range at each step
    climbing_variable(n, jump_array)