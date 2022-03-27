# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful
# Medium
# T = O(N)
# S = O(1)
from typing import List


def minDeletion(nums: List[int]) -> int:
    res = 0

    for i in range(len(nums) - 1):
        if (i + res) % 2 == 0 and nums[i] == nums[i + 1]:
            res += 1

    if (len(nums) - res) % 2 == 1:
        res += 1

    return res


# More intuitive
def minDeletionGreedy(A):
    res = []
    for a in A:
        if len(res) % 2 == 0 or a != res[-1]:  # add greedily to another array elligible elements
            res.append(a)
    return len(A) - (len(res) - len(res) % 2)
