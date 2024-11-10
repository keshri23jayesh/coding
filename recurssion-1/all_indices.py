
def all_indices(arr, occ, idx):
    if len(arr) == idx:
        return 0
    ans = all_indices(arr, occ, idx+1)
    if occ == arr[idx]:
        return ans + 1
    return ans


arr = [2, 3, 4, 5, 6, 7, 4, 5]
print(all_indices(arr, 6, 0))