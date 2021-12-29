from collections import Counter


# https://leetcode.com/problems/valid-anagram/
# Easy
# T = O(N)
# S = O(N)

def isAnagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counter = Counter()
    for i in range(len(s)):
        counter[s[i]] += 1
        counter[t[i]] -= 1

    for v in counter.values():
        if v != 0:
            return False
    return True


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
