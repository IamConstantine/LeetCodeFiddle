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
    list_of_combs = []
    length = len(candidates)

    def combinationSumInner(rem: int, l, start):
        if rem == 0:
            list_of_combs.append(list(l))
            return l
        if rem < 0:
            return

        for index in range(start, length):
            x = candidates[index]
            l.append(x)
            combinationSumInner(rem - x, l, index)
            l.pop()
            index += 1

    combinationSumInner(target, [], 0)
    return list_of_combs

