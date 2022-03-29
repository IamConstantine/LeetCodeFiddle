from typing import List


# https://leetcode.com/problems/find-the-duplicate-number
# Medium

# T = O(N)
# S = O(1)
# using Floyd's Cycle Detection Algorithm
# I can this because the value of numbers in array are positive and in the range of 1 to n+1
# So when I make the jump using value as index, I will always land on another index in the range.

def findDuplicateFloyd(nums: List[int]) -> int:
    hare = tortoise = nums[0]

    while True:
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]
        if hare == tortoise:
            break

    tortoise = nums[0]
    while tortoise != hare:
        hare = nums[hare]
        tortoise = nums[tortoise]

    return hare


# T = O(N)
# S = O(1)
# Genius Algorithm which makes use of positive numbers constraint to figure out the solution

def findDuplicate(nums: List[int]) -> int:
    res = -1

    for num in nums:
        idx = abs(num)
        if nums[idx] < 0:
            res = idx
            break

        nums[idx] = -nums[idx]

    for i in range(len(nums)):
        nums[i] = abs(nums[i])

    return res
