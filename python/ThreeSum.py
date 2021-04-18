from typing import List


def twoSum(sorted_nums: List[int], n: int, i, res: List[List[int]]):
    j = len(sorted_nums) - 1
    while i < j:
        sum = sorted_nums[i] + sorted_nums[j]
        if sum < -n:
            i += 1
        elif sum > -n:
            j -= 1
        else:
            res.append([n, sorted_nums[i], sorted_nums[j]])
            i += 1
            j -= 1
            while i < j and sorted_nums[i] == sorted_nums[i - 1]:  # skip consecutive same values
                i += 1


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i] != nums[i - 1]:  # remove already calculated ones
            twoSum(nums, nums[i], i + 1, result)
    return result
