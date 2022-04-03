# https://leetcode.com/problems/next-permutation
# Medium
# T = O(N)
# S = O(1)
from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    i = len(nums) - 2

    # find first decreasing element from the last
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1

    if i >= 0:
        # swap the element with the first element greater than ith from last
        j = len(nums) - 1

        while nums[i] >= nums[j]:
            j -= 1

        nums[j], nums[i] = nums[i], nums[j]

    # reverse the rest
    j = len(nums) - 1
    i = i + 1
    while i < j:
        nums[j], nums[i] = nums[i], nums[j]
        i += 1
        j -= 1
