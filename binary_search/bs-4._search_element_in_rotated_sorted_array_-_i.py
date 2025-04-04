# https://www.youtube.com/watch?v=5qGrJbHhqFs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=5

arr = [7,8,9,1,2,3,4,5,6]
target = 1


def find_elem_in_rotated_sorted_array(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
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

print(find_elem_in_rotated_sorted_array(arr, target))

