from typing import List

#https://leetcode.com/problems/counting-bits

def countBits(n: int) -> List[int]:
    ans = []
    for i in range(n + 1):
        ans.append(countSetBits(i))
    return ans


def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def dp_countBits(n: int):
    ans = [0] * (n + 1)
    for x in range(1, n + 1):
        # P(x) = P(x / 2) + (x mod 2)(LSB)
        ans[x] = ans[x >> 1] + (x & 1)
    return ans
