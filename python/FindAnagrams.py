from collections import Counter
from typing import List


# https://leetcode.com/problems/find-all-anagrams-in-a-string
# Medium
# T = O(Np + Ns)
# S = O(1)

def findAnagrams(s: str, p: str) -> List[int]:
    s_len, p_len = len(s), len(p)

    res = []
    p_count = Counter(p)
    s_count = Counter()

    for i in range(s_len):
        s_count[s[i]] += 1

        if i >= p_len:
            if s_count[s[i - p_len]] == 1:
                del s_count[s[i - p_len]]
            else:
                s_count[s[i - p_len]] -= 1
        if p_count == s_count:
            res.append(i - p_len + 1)

    return res
