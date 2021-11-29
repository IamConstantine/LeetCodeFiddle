from typing import List

# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Medium

def search(nums: List[int], target: int) -> int:
    def rotatedSearch(l, u):
        if l > u:
            return -1

        mid = (l + u) >> 1
        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                return rotatedSearch(l, mid - 1)
            return rotatedSearch(mid + 1, u)

        if nums[mid] < target <= nums[u]:
            return rotatedSearch(mid + 1, u)
        return rotatedSearch(l, mid - 1)

    return rotatedSearch(0, len(nums) - 1)
