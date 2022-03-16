from typing import List


# https://leetcode.com/problems/validate-stack-sequences
# Medium
# T = O(N)
# S = O(N)

# greedy
def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    j = 0
    stck = []

    for x in pushed:
        stck.append(x)

        while stck and j < len(popped) and stck[-1] == popped[j]:
            stck.pop()
            j += 1

    return j == len(popped)
