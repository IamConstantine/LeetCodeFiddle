from typing import List


# https://leetcode.com/problems/subarray-sum-equals-k
# Medium
# T = O(N)
# S = O(N)

# sliding window wont work has it has negatives
# if the difference in cumulative sum between i and j equals k, then there is a subarray between i and j which equals k
# sum(i) - sum(j) = k means sum(i, j) = k

def subarraySum(nums: List[int], k: int) -> int:
    add, count = 0, 0
    cumulative_sum = {0: 1}  # We initialize with 0 to handle same k value or zero. Eg: k is 0 or 7 and nums has 0 or 7
    for i in range(len(nums)):
        add += nums[i]
        if add - k in cumulative_sum:
            count += cumulative_sum[add - k]  # add all occurences as well

        cumulative_sum[add] = cumulative_sum.get(add, 0) + 1

    return count
