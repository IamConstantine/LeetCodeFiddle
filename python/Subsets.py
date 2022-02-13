from typing import List


# https://leetcode.com/problems/subsets
# Medium
# T = O(N * 2 ^ N) - n iterations and 2 * N to compute the subset(absent or present choice)
# S = O(N * 2 ^ N)
def subsets(nums: List[int]) -> List[List[int]]:
    l = [[]]
    for num in nums:
        l += [curr + [num] for curr in l]
    return l
