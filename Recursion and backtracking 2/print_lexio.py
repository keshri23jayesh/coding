

def dfs(i, n):
    if i > n:
        return

    print(i)
    for j in range(1,10):
        dfs(10*i + j, n)


n = 1000
for i in range (1, 10):
    dfs(i,n)