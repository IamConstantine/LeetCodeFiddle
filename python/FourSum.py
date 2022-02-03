from collections import Counter
from typing import List


# https://leetcode.com/problems/4sum-ii
# Medium

# T = O(n**2)
# S = O(n**2)

def fourSumCount_special(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    cnt = 0

    add = Counter(x + y for x in nums1 for y in nums2)

    for x in nums3:
        for y in nums4:
            if -(x + y) in add:
                cnt += add[-(x + y)]

    return cnt


# T = O(n**(k//2))
# S = O(n**(k//2))
# Generic solution for kSum

def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    counter = Counter()

    def addHash(lists, index, add):
        if index == len(lists) // 2:
            counter[add] += 1
        else:
            for x in lists[index]:
                addHash(lists, index + 1, add + x)

    def countComplements(lists, index, complement):
        if index == len(lists):
            return counter[complement]
        cnt = 0
        for x in lists[index]:
            cnt += countComplements(lists, index + 1, complement - x)
        return cnt

    def kSumCount(lists):
        addHash(lists, 0, 0)
        return countComplements(lists, len(lists) // 2, 0)

    return kSumCount([nums1, nums2, nums3, nums4])
