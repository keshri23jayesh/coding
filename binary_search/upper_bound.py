from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    ans = nums[-1]
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            ans = mid
            high = mid - 1  # Target might be at mid or to the left, so move high
        else:
            low = mid + 1  # Target is on the right, move low up

    return ans  # This is the index of the first element >= target


def upper_bound(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums)
    ans = nums[-1]
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            ans = mid
            high = mid-1  # Target might be at mid or to the left, so move high
        else:
            low = mid + 1  # Target is on the right, move low up

    return ans  # This is the index of the first element > target


# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8

lb = lower_bound(nums, target)
ub = upper_bound(nums, target)

print(f"Lower bound index for {target}: {lb}")
print(f"Upper bound index for {target}: {ub}")
print(f"Indices of occurrences of {target}: [{lb}, {ub - 1}]")
