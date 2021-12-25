from typing import List


# https://leetcode.com/problems/word-break
# Medium
# T = O(n^3) - at every index, we perform O(N^2) comparisons
# S = O(n)
# There are some discussions in its thread regarding using Trie for this problem

def wordBreak(s: str, wordDict: List[str]) -> bool:
    length = len(s)
    word_set = frozenset(wordDict)

    # @lru_cache
    def wordBreakInner(start, memo={}):
        if start == length:
            return True

        if start in memo:
            return memo[start]

        end = start + 1
        while end <= length:
            if s[start: end] in word_set and wordBreakInner(end, memo):
                memo[start] = True
                return True
            end += 1
        memo[start] = False
        return False

    return wordBreakInner(0)
