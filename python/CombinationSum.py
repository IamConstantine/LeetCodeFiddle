from typing import List


# https://leetcode.com/problems/combination-sum
# Medium
# Time complexity : O(N^T/M) where N is number of candidates, T is target and M is smallest element of the array.
# T/M would give you the max height of the tree
# So the actual no of nodes in N ary tree of height T/M would N^T/M+1
#
# The space complexity is O(N^T/M).
# The number of recursive calls can pile up to N^T/M. As a result, the space overhead of the recursion is O(N^T/M).
# In addition, we keep a combination of numbers during the execution, which requires at most O(N^T/M) space as well.
# Also the space used to hold the final results for the space complexity.

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def combinationSumInner(n, l, start):
        if target < n:
            return
        if target == n:
            return res.append(l)

        for i in range(start, len(candidates)):
            combinationSumInner(n + candidates[i], l + [candidates[i]], i)

    combinationSumInner(0, [], 0)
    return res
