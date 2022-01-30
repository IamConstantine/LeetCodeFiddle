from typing import List

# https://leetcode.com/problems/rotate-array
# Medium
# T = O(N)
# S = O(1)
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    length = len(nums)

    k = k % length

    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(nums, 0, length - 1)

    reverse(nums, 0, k - 1)
    reverse(nums, k, length - 1)