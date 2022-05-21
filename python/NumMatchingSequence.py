from collections import defaultdict
from typing import List


# https://leetcode.com/problems/number-of-matching-subsequences
# Medium
# T = O(len(s) + sum of length of all words)
# S = O(len(words))

# Use next letter pointers
def numMatchingSubseq(s: str, words: List[str]) -> int:
    cache = defaultdict(list)

    for it in map(iter, words):
        cache[next(it)].append(it)

    for c in s:
        for it in cache.pop(c, ()):
            cache[next(it, None)].append(it)

    return len(cache[None])
