from typing import List


# https://leetcode.com/problems/can-place-flowers
# Easy
# T = O(n)
# S = O(1)

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    prev = -2  # an imaginary flowerplot before 0th index
    i = 0

    while n > 0 and i < len(flowerbed):
        if flowerbed[i] == 1:
            n -= (i - prev - 2) // 2  # find no of empty plots we can use
            prev = i
        i += 1

    n -= (i - 1 - prev) // 2
    return n <= 0
