# https://www.youtube.com/watch?v=rjEJeYCasHs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=12


def is_nth_root(N, M, mid):
    ans = 1
    for i in range(1, M+1):
        ans *= mid
    if ans == N:
        return 1
    if ans > N:
        return 2
    if ans < N:
        return 3


def find_nth_root(N, M):
    low = 1
    high = N
    while low <= high:
        mid = (low + high)//2
        ans = is_nth_root(N, M, mid)
        if ans == 1:
            return mid
        elif ans ==2:
            high = mid - 1
        elif ans == 3:
            low = mid + 1
    return -1

print(find_nth_root(81, 4))
