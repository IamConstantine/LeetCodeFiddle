from typing import List


# https://leetcode.com/problems/longest-common-prefix
# Marked Easy but dont think so
# T + O(S) - total no of chars from all strings
# S = O(S) - all chars of string

class LongestCommonPrefix:
    def __init__(self):
        self.trie = {}

    def add_word(self, word):
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]

        node['$'] = True

    def search_longest_prefix(self):
        result = ''
        node = self.trie
        while node:
            if len(node) != 1 or '$' in node:
                return result

            c, node = next(iter(node.items()))
            result += c

    def longestCommonPrefix(self, strs: List[str]) -> str:
        for x in strs:
            self.add_word(x)

        return self.search_longest_prefix()


def another_solution(strs):
    idx = 0
    for group in zip(*strs):
        if len(set(group)) != 1:
            return strs[0][:idx]
        idx += 1

    return strs[0][:idx]
