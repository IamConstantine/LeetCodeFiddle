from typing import List


# https://leetcode.com/problems/monotonic-array
# Easy
# T + O(N)
# S = O(1)

def isMonotonic(nums: List[int]) -> bool:
    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            increasing = False
        elif nums[i - 1] < nums[i]:
            decreasing = False

    return increasing or decreasing
