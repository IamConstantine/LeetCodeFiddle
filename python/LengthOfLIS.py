from bisect import bisect_left
from typing import List


# https://leetcode.com/problems/longest-increasing-subsequence
# Medium
# T = O(N^2) - a slow approach using DP
# S = O(N)

def lengthOfLIS_dp(nums: List[int]) -> int:
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# T = O(nlogn) - use Binary search instead of linear scan to figure out the position and update the sequence

def lengthOfLIS(nums: List[int]) -> int:
    sub = []
    for num in nums:
        i = bisect_left(sub, num)

        # If num is greater than any element in sub
        if i == len(sub):
            sub.append(num)

        # Otherwise, replace the first element in sub greater than or equal to num
        else:
            sub[i] = num

    return len(sub)
