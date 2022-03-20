from typing import List


# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row
# Medium
# T = O(N)
# S = O(1)

# Greedy solution
def minDominoRotations(tops: List[int], bottoms: List[int]) -> int:
    # as we want to make the whole side of same value,
    # the candidates can be narrowed down to elements at any arbitrary index.
    # In our case, we pick 0th element
    valid_numbers = [tops[0], bottoms[0]]

    for x in valid_numbers:

        count_top = 0
        count_bottom = 0

        for i in range(len(tops)):
            if x != tops[i] and x != bottoms[i]:  # If doesn't match, rotation with x is not possible.
                break
            count_top += (x == tops[i])
            count_bottom += (x == bottoms[i])

        if i == len(tops) - 1:
            return len(tops) - max(count_top, count_bottom)

    return -1
