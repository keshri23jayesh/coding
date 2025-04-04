# https://www.youtube.com/watch?v=w2G2W8l__pc&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=6


def find_target(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid

        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        elif arr[low] <= arr[mid]:
            # left half sorted and target on this part
            if arr[low] <= target <= arr[mid]:
                high = mid
            else:
                low = mid
        elif arr[mid] <= arr[high]:
            # right half sorted and target on this part
            if arr[mid] <= target <= arr[high]:
                low = mid
            else:
                high = mid
    return -1

arr = [3,3,1,2,3,3,3,3]
target = 1

print(find_target(arr, target))