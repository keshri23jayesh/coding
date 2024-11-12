
def last_occurrence(arr, occ, idx):
    if len(arr) == idx:
        return -1
    last_occ = last_occurrence(arr, occ, idx + 1)
    if last_occ and last_occ != -1:
        return last_occ
    if arr[idx] == occ and idx > last_occ:
        return idx
    else:
        return -1


arr = [2, 3, 4, 5, 6, 7, 4, 5]
print(last_occurrence(arr, 9, 0))
