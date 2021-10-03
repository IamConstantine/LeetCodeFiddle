from typing import List


# https://leetcode.com/problems/maximum-subarray

def maxSubArray(nums: List[int]) -> int:
    max_sum = -10000
    length_of_nums = len(nums)
    if length_of_nums == 1:
        return nums[0]
    sum = 0
    for i in range(length_of_nums):
        sum = max(nums[i], sum + nums[i])
        max_sum = max(max_sum, sum)
    return max_sum


def maxSubArray_bruteForce(nums: List[int]) -> int:
    max = -10000
    length_of_nums = len(nums)
    if length_of_nums == 1:
        return nums[0]
    for i in range(length_of_nums):
        sum = nums[i]
        for j in range(i + 1, length_of_nums):
            sum = sum + nums[j]
            if sum > max:
                max = sum
    return max
