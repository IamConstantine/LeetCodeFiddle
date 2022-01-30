import collections
from typing import List


# https://leetcode.com/problems/group-shifted-strings
# Medium
# T = O(N * K) - K is max length of string
# S = O(N * K) - K is max length of string. It stores hash key and string

def groupStrings(strings: List[str]) -> List[List[str]]:
    res = collections.defaultdict(list)
    for string in strings:
        encoding = ''
        for i in range(len(string) - 1):
            encoding += str((ord(string[i]) - ord(string[i + 1])) % 26)
        res[encoding].append(string)

    return list(res.values())
