# https://leetcode.com/problems/get-maximum-in-generated-array/

def getMaximumGenerated(n):
    if n == 0 or n == 1:
        return n

    nums = [0] * (n + 1)
    nums[1] = 1
    max_num = 0
    for i in range(2, n + 1):
        if i % 2 == 0:
            nums[i] = nums[i // 2]
        else:
            nums[i] = nums[i // 2] + nums[i // 2 + 1]
        max_num = max(max_num, nums[i])
    return max_num
