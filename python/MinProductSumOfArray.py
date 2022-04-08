from collections import Counter
from typing import List


# https://leetcode.com/problems/minimize-product-sum-of-two-arrays
# Medium
# T = O(n + k) where k is range of count array which 1 to 100
# S = O(k)

def minProductSum(nums1: List[int], nums2: List[int]) -> int:
    counter1, counter2 = Counter(nums1), Counter(nums2)

    p1 = 1
    p2 = 100

    ans = 0
    while p1 <= 100 and p2 > 0:

        while p1 <= 100 and counter1[p1] == 0:
            p1 += 1

        while p2 > 0 and counter2[p2] == 0:
            p2 -= 1

        if p1 > 100 or p2 == 0:
            break

        occ = min(counter1[p1], counter2[p2])

        ans += occ * p1 * p2
        counter1[p1] -= occ
        counter2[p2] -= occ

    return ans


def minProductSumSorted(nums1: List[int], nums2: List[int]) -> int:
    nums1.sort()
    nums2.sort(reverse=True)

    return sum(x * y for x, y in zip(nums1, nums2))
