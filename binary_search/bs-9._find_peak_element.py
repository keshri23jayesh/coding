# https://www.youtube.com/watch?v=cXxmbemS6XM&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=10


arr = [1,10,13,7,6,5,4,2,1,0]

def find_peak(arr):
    n = len(arr)
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n-1] > arr[n-2]:
        return arr[n-1]
    low = 1
    high = len(arr) - 2
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid - 1]  and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(find_peak(arr))