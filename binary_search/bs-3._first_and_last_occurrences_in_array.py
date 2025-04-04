# https://www.youtube.com/watch?v=hjR1IYVx9lY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=4


def find_first_occ(array, elem):
    low = 0
    high = len(array)-1
    ans = -1
    while low < high:
        mid = (low + high)//2
        if array[mid] == elem:
            ans = mid
            high = mid - 1
        elif array[mid] > elem:
            high = mid - 1
        elif array[mid] < elem :
            low = mid + 1
    return ans

def find_last_occ(array, elem):
    low = 0
    high = len(array)-1
    ans = -1
    while low < high:
        mid = (low + high)//2
        if array[mid] == elem:
            ans = mid
            low = mid + 1
        elif array[mid] > elem:
            high = mid - 1
        elif array[mid] < elem :
            low = mid + 1
    return ans



array = [2,3,3,5,5,5,5,6,7,8,10]
elem = 5
print(find_first_occ(array, elem))
print(find_last_occ(array, elem))