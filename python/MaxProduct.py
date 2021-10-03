from typing import List


# https://leetcode.com/problems/maximum-product-subarray

# O(n) simple solution using two passes of the array. One in forward direction. One in backward direction.
def maxProduct_easy(nums: List[int]) -> int:
    max_product = int(- ((2 ** 32) / 2))
    product = 1
    for i in range(len(nums)):
        product = product * nums[i]
        max_product = max(max_product, product)
        if product == 0:
            product = 1
    product = 1
    for i in range(len(nums) - 1, 0, -1):
        product = product * nums[i]
        max_product = max(max_product, product)
        if product == 0:
            product = 1
    return max_product


# DP tricky O(n)
def maxProduct(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    result = min_so_far = max_so_far = nums[0]

    for i in range(1, len(nums)):
        temp = max(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
        min_so_far = min(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)

        max_so_far = temp
        result = max(result, max_so_far)
    return result
