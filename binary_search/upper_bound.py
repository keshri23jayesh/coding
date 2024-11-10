# from typing import List
#
#
# from typing import List
#
#
# def upper_bound(nums: List[int], target: int) -> int:
#     low = 0
#     high = len(nums)
#     while low < high:
#         mid = low + (high - low) // 2
#         if nums[mid] > target:
#             high = mid  # Continue searching on the left side
#         else:
#             low = mid + 1  # Search on the right side
#     print(low)
#     return low  # Return the upper bound index
#
#
# def lower_bound(nums: List[int], target: int) -> int:
#     low = 0
#     high = len(nums)
#     while low < high:
#         mid = low + (high - low) // 2
#         if nums[mid] >= target:
#             high = mid  # Continue searching on the left side
#         else:
#             low = mid + 1  # Search on the right side
#     print(low)
#     return low  # Return the lower bound index
#
#
# upper_bound([5, 7, 7, 8, 8, 10], 8)
# lower_bound([5, 7, 7, 8, 8, 10], 8)

from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums)

    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            high = mid  # Target might be at mid or to the left, so move high
        else:
            low = mid + 1  # Target is on the right, move low up

    return low  # This is the index of the first element >= target


def upper_bound(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums)

    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid  # Target might be at mid or to the left, so move high
        else:
            low = mid + 1  # Target is on the right, move low up

    return low  # This is the index of the first element > target


# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8

lb = lower_bound(nums, target)
ub = upper_bound(nums, target)

print(f"Lower bound index for {target}: {lb}")
print(f"Upper bound index for {target}: {ub}")
print(f"Indices of occurrences of {target}: [{lb}, {ub - 1}]")
