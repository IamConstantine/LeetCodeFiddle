# https://leetcode.com/problems/brace-expansion
# Medium
# T = O(N * 3 ** N/7) - not sure how
# S = O(N) - stack depth is equal to the length of the word

from typing import List


def expand(s: str) -> List[str]:
    options = []
    idx = 0

    while idx < len(s):
        if s[idx] == '{':
            idx += 1
            x = ''
            while s[idx] != '}':
                if s[idx].islower():
                    x += s[idx]
                idx += 1
            options.append(sorted(x))
        else:
            options.append(s[idx])
        idx += 1

    res = []

    def findAll(options_idx, st):
        if options_idx == len(options):
            res.append(st)
            return

        for c in options[options_idx]:
            findAll(options_idx + 1, st + c)

    findAll(0, '')
    return res
