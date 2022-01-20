from typing import List


# https://leetcode.com/problems/koko-eating-bananas
# Medium
# T = O(NlogM) - n - no of piles and m is maximum no of bananas in a pile
# S = O(1)

def minEatingSpeed(piles: List[int], h: int) -> int:
    def checkIfPossible(k):
        cnt = 0

        for x in piles:
            cnt += ((x - 1) // k) + 1  # ceil

        return cnt <= h  # sum((pile - 1) // speed + 1 for pile in piles) <= h

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if checkIfPossible(mid):
            right = mid  # should be mid instead mid - 1
        else:
            left = mid + 1
    return left
