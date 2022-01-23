from typing import List


# https://leetcode.com/problems/sequential-digits
# Medium
# T = O(1) - the loop always runs atmost 8 * 8 times because min starts 12
# S = O(1), output array is ignored

def sequentialDigits(low: int, high: int) -> List[int]:
    sample = '123456789'
    nums = []

    for length in range(len(str(low)), len(str(high)) + 1):
        for start in range(10 - length):
            num = int(sample[start: start + length])
            if low <= num <= high:
                nums.append(num)
    return nums
