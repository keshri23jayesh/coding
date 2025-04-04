# https://www.youtube.com/watch?v=TXAuxeYBTdg&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=14


bloom_day = [7, 7, 7, 7, 13, 11, 12, 7]
n = 2
k = 3

def is_day_valid(mid, n, k):
    bcount = 0
    cnt = 0
    for day in bloom_day:
        if day <= mid:
            cnt += 1
        else:
            bcount += cnt//k
            cnt = 0
    if cnt > 0:
        bcount += cnt // k
        cnt = 0

    if bcount >= n:
        return True
    else:
        return False


def find_min_days(n, k):
    low = min(bloom_day)
    high = max(bloom_day)
    ans = high
    while low <= high:
        mid = (low + high)//2
        is_valid = is_day_valid(mid, n, k)
        if is_valid:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

print(find_min_days(n, k))