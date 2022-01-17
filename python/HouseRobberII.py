from typing import List


# https://leetcode.com/problems/house-robber-ii
# Medium
# T = O(N)
# S = O(1)

def rob_ii(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    return max(rob_i(nums[1:]), rob_i(nums[:-1]))


def rob_i(arr):
    a = 0
    b = 0
    for n in arr:
        c = max(n + a, b)
        a = b
        b = c
    return b
