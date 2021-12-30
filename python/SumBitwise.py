# https://leetcode.com/problems/sum-of-two-integers
# Medium
# Read the Solution section for approach 2
def getSum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    while b != 0:
        carry = ((a & b) << 1) & mask
        # this mask is invisible in Java as it uses 2s complement for representing numbers
        a = (a ^ b) & mask
        b = carry

    max_int = 0x7FFFFFFF
    return a if a < max_int else ~(a ^ mask)
