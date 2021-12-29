from typing import List


# https://leetcode.com/problems/product-of-array-except-self
# Medium

# T = O(N)
# S = O(N)

def productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)
    left, right, output = [1] * length, [1] * length, [1] * length

    for i in range(1, length):
        right[i] = nums[i - 1] * right[i - 1]

    for i in range(length - 2, -1, -1):
        left[i] = nums[i + 1] * left[i + 1]

    for i in range(length):
        output[i] = left[i] * right[i]
    return output


# T = O(N)
# S = O(1) - Calculate left and then calculate right on the fly

def productExceptSelf_withS1(nums: List[int]) -> List[int]:
    length = len(nums)
    output = [1] * length

    for i in range(1, length):
        output[i] = nums[i - 1] * output[i - 1]

    r_product = 1
    for i in range(length - 1, -1, -1):
        output[i] = output[i] * r_product
        r_product *= nums[i]

    return output


# Invalid for the stated problem as it wants a solution without division operator
def productExceptSelf_with_div(nums: List[int]) -> List[int]:
    product = 1
    zero_value_index = -1
    for i in range(len(nums)):
        if nums[i] != 0:
            product *= nums[i]
        elif zero_value_index != -1:
            return [0] * len(nums)
        else:
            zero_value_index = i

    output = [0] * len(nums)
    if zero_value_index != -1:
        output[zero_value_index] = product
        return output

    for i in range(len(nums)):
        output[i] = product / nums[i]

    return output
