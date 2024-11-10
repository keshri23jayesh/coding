from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    i = 0
    j = 0
    nums1[i] = set()
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            final_set.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return list(nums1[i])


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
intersection(nums1, nums2)