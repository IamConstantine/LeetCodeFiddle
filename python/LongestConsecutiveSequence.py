from typing import List


# https://leetcode.com/problems/longest-consecutive-sequence
# Medium
# T = O(N) - The inner loop is only triggered when the current element is head of the sequence i.e min value of the sequence
# S = O(N) - Due to the Hashset

def longestConsecutive(nums: List[int]) -> int:
    streak = 0
    nums_set = set(nums)  # also allows to eliminate duplicates
    for value in nums_set:
        if value - 1 not in nums_set:
            curr_streak = 0
            while value + curr_streak in nums_set:
                curr_streak += 1
            streak = max(streak, curr_streak)
    return streak
