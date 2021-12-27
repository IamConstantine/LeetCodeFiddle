# https://leetcode.com/problems/reverse-bits
# Easy
# T = O(1)
# S = O(1)

def reverseBits(n: int):
    num = 0
    power = 31  # the input is 32 bit
    while n:
        num += (n & 1) << power
        n >>= 1
        power -= 1
    return num
