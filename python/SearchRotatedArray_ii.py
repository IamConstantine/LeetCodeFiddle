from typing import List


# https://leetcode.com/problems/search-in-rotated-sorted-array-ii
# Medium
# T = O(logN)
# S = O(1)

def search(nums: List[int], target: int) -> bool:
    l = 0
    u = len(nums) - 1

    while l <= u:

        mid = (l + u) >> 1

        if nums[mid] == target:
            return True

        # getting away from duplicates
        if nums[l] == nums[mid]:
            l += 1
            continue  # and calculate new mid

        # check if mid might be present in first array
        mid_array = nums[l] <= nums[mid]
        # check if target might be present in first array
        target_array = nums[l] <= target

        # check if only one of them is true
        if mid_array ^ target_array:
            # if target is present in first array
            # and mid is part of rotated tail
            if target_array:
                u = mid - 1
            else:
                l = mid + 1
        else:  # if mid and target both exist in lower array

            # if target is in second array
            if nums[mid] < target:
                l = mid + 1
            else:
                u = mid - 1

    return False
