# https://www.youtube.com/watch?v=UvBKTVaG6U8&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=15
import math

def find_sum(arr, mid):
    sum = 0
    for elem in arr:
        sum += math.ceil(elem/mid)
    return sum


def find_smallest_divisior_of_given_threshold(arr, threshold):
    low = 1
    high = 9
    ans = high
    while low <= high:
        mid = (low + high)//2
        current_sum = find_sum(arr, mid)
        if current_sum <= threshold:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [1,2,5,9]
threshold_sum = 6

print(find_smallest_divisior_of_given_threshold(arr, threshold_sum))









