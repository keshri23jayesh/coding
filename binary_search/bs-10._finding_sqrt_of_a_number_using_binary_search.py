# https://www.youtube.com/watch?v=Bsv3FPUX_BA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=11


def find_squart(num):
    low = 1
    high = num // 2
    while low <= high:
        mid = (low+high) // 2
        if mid * mid == num:
            return mid
        elif mid * mid < num:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(find_squart(25))
