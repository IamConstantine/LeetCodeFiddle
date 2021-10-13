from typing import List


# https://leetcode.com/problems/split-array-largest-sum

def splitArray(nums: List[int], m: int) -> int:
    return splitArray(nums, 0, len(nums), m, {})


def splitArray(nums: List[int], start: int, end: int, m: int, mem: [str, int]) -> int:
    if end - start < m:
        return -1

    i = start
    max_sum = 0
    if f'{i}_{start + m}' in mem:
        return mem[f'{i}_{start + m}']

    while i < start + m:
        max_sum = max_sum + nums[i]
        i += 1
    mem[f'{start}_{i}'] = max_sum

    start_index = 0
    end_index = i
    while end_index < len(nums):
        end_index += 1
    for i in range(m, len(nums)):
        start_index = i - m
        end_index = m

        pass
    return 0
