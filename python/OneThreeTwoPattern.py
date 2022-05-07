import math
from typing import List


# https://leetcode.com/problems/132-pattern
# Medium
# T = O(N)
# S = O(N)

def find132pattern_better(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    second_num = -math.inf
    stck = []
    # Try to find nums[i] < second_num < stck[-1]
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < second_num:
            return True
        # always ensure stack can be popped in increasing order
        while stck and stck[-1] < nums[i]:
            second_num = stck[-1]  # this will ensure  second_num < stck[-1]  for next iteration
            stck.pop()

        stck.append(nums[i])

    return False


def find132pattern(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    min_array = [-1] * len(nums)
    min_array[0] = nums[0]

    for i in range(1, len(nums)):
        min_array[i] = min(min_array[i - 1], nums[i])

    stck = []

    # trying to find min_array[i] < stck[-1] < nums[i]
    # we will find two parts:
    # 1. min_array[i] < stck[-1]
    # 2. stck[-1] < nums[i]

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] <= min_array[i]:  # if equal or less than min, skip
            continue

        # after pop operations, we will have min_array[i] < stck[-1] (first part)
        while stck and stck[-1] <= min_array[i]:
            stck.pop()

        if stck and stck[-1] < nums[i]:  # check second part
            return True

        stck.append(nums[i])

    return False
