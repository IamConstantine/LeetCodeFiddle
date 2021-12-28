from typing import List


# https://leetcode.com/problems/house-robber
# Medium
# T = O(N)
# S = O(1) - A DP problem but doesnt need a DP array because we do only upto 2 index look back.

def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    a = nums[0]
    b = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        c = max(nums[i] + a, b)
        a = b
        b = c
    return b


# S = O(2N) - call stack and map

def rob_recur(nums: List[int]) -> int:
    mem = {}

    def robInner(start):
        nonlocal mem
        if start >= len(nums):
            return 0

        if start in mem:
            return mem[start]

        max_amount = max(nums[start] + robInner(start + 2), robInner(start + 1))

        mem[start] = max_amount
        return max_amount

    return robInner(0)
