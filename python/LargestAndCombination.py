from typing import List


# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero
# Medium
# T = O(nlog10000000)
# S = O(1)

# the main idea is to find number of elements with bit set at each position
# As the max value in the array is bound to 10^7, we need atmost 24 bits to represent this
# and can be used to find all set bits

def largestCombination(candidates: List[int]) -> int:
    return max(sum((x >> i) & 1 for x in candidates) for i in range(24))
