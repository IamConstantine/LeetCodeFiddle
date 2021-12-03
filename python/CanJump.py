from typing import List


# https://leetcode.com/problems/jump-game
# Medium

# Best approach is using Greedy and go bottom up
# T = 0(n) and S = O(1)

def canJump(nums: List[int]) -> bool:
    if 0 not in nums: # if no O, its already solved
        return True
    lastPos = len(nums) - 1

    for i in range(lastPos - 1, -1, -1):
        if (i + nums[i]) >= lastPos:
            lastPos = i

    return lastPos == 0


# the python DP(top down) solution seems to LC timeout. The java one did - weird
# T = O(n ^ 2) for every i, we traverse the right of i
# S = O(2n) - one for recursion and another for memo

def canJumpDPTD(nums: List[int]) -> bool:
    upper = len(nums)
    mem = [-1] * upper

    mem[-1] = 1

    def canJumpInner(curr):
        if mem[curr] != -1:
            return True if mem[curr] == 1 else False

        upper_limit = min(nums[curr] + curr, upper - 1)
        for i in range(curr + 1, upper_limit + 1):
            if canJumpInner(i):
                mem[curr] = 1
                return True
        mem[curr] = 0
        return False

    return canJumpInner(0)


# DP bottom up with S = O(n) - Poor timings for this as well
def canJumpDP(nums: List[int]) -> bool:
    upper = len(nums)
    mem = [-1] * upper

    mem[-1] = 1

    for i in range(upper - 2, -1, -1):
        upper_limit = min(i + nums[i], upper - 1)
        for j in range(i + 1, upper_limit + 1):
            if mem[j] == 1:
                mem[i] = 1
                break

    return mem[0] == 1
