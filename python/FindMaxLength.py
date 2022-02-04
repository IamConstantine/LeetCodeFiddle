from typing import List


# https://leetcode.com/problems/contiguous-array
# Medium
# T = O(N)
# S = O(N)

def findMaxLength(nums: List[int]) -> int:
    # Initialize map with count 0 and index -1
    map = {0: -1}

    max_length = 0
    count = 0

    for i in range(len(nums)):
        count = count + (1 if nums[i] == 1 else -1)  # offset based on value

        # if a count is encountered again during iteration, it means there is same number of zeroes and ones between
        # count index and i
        # eg: index 2 count is -2 and then you encounter count -2 again at index 6. It means we have same count of 0s
        # and 1s between  index 2 and 6

        if count in map:
            max_length = max(max_length, i - map[count])
        else:
            map[count] = i
    return max_length
