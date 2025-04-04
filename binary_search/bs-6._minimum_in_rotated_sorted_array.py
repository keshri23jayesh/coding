# https://www.youtube.com/watch?v=nhEMDKMB44g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=7
import math

arr = [4,5,6,7,0,1,2]
arr = [4,5,6,7,8,9,10,11,1,2,3]


def find_min_in_arr(arr):
    min_elem = 100000
    min_idx = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[low] <= arr[mid]:
            if min_elem < arr[low]:
                min_elem = arr[low]
                min_idx = low
            low = mid + 1
        else:
            if min_elem < arr[mid]:
                min_elem = arr[mid]
                min_idx = mid
            min_elem = min(min_elem, arr[mid])
            high = mid - 1
    return min_idx

print(find_min_in_arr(arr))