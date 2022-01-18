from typing import List


# https://leetcode.com/problems/maximize-distance-to-closest-person
# Medium
# T = O(N)
# S = O(1)

def maxDistToClosest(seats: List[int]) -> int:
    i = 0
    while i < len(seats) and seats[i] == 0:
        i += 1
    prev = i

    maxDist = prev
    while i < len(seats):
        if seats[i] == 1:
            maxDist = max((i - prev) // 2, maxDist)
            prev = i
        i += 1
    return max(len(seats) - 1 - prev, maxDist)
