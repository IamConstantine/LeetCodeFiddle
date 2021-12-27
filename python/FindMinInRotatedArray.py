import sys
from typing import List


# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
# Medium
# T = O(logN) - as its a Binary Search
# S = O(1)

def findMin(nums: List[int]) -> int:
    l = 0
    u = len(nums) - 1
    if nums[l] < nums[u]:
        return nums[l]

    while l + 1 < u:  # because I am not shifting by 1 the mid for each iteration, my termination condition is +1
        mid = (l + u) >> 1

        if nums[l] > nums[mid]:
            u = mid
        else:
            l = mid

    return nums[u]


def first_findMin(nums):
    l = 0
    u = len(nums) - 1
    minimum = sys.maxsize
    while l <= u:
        mid = (l + u) >> 1

        minimum = min(minimum, nums[mid])
        if nums[l] <= nums[mid] > nums[u]:
            l = mid + 1
        else:
            u = mid - 1
    return minimum
