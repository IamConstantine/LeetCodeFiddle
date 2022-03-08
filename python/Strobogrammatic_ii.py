from typing import List


# https://leetcode.com/problems/strobogrammatic-number-ii
# Medium
# T = O(N * 5 ** (N/2 + 1)) - The depth is n/2 because we increment by 2 at each level.
# The + 1 is for empty or (1 len string) level based on evenness of n
# At each level, we have to go through 5 pairs to form the substring.
# At each level, we perform append operation. Append at the start of string takes O(N) time

# S = O(N * 5 ** (N/2))

def findStrobogrammatic(n: int) -> List[str]:
    pairs = [
        ['0', '0'], ['1', '1'],
        ['6', '9'], ['8', '8'], ['9', '6']
    ]

    q = ['0', '1', '8'] if n & 1 else ['']

    i = n % 2  # start point as in 1 or 0 depending on n

    while i < n:
        next_level = []
        i += 2  # its moved before actual list creation to avoid '000' case

        for num in q:
            for pair in pairs:
                if n != i or pair[0] != '0':
                    next_level.append(pair[0] + num + pair[1])
        q = next_level

    return q
