# https://leetcode.com/problems/design-add-and-search-words-data-structure
# Medium
# T = O(M) - add key length, search = O(M) for search without dots and O(N.26 ^ M)
# S = O(1) - for search without dots and O(M) for search with dots
class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        ptr = self.trie
        for ch in word:
            if ch not in ptr:
                ptr[ch] = {}
            ptr = ptr[ch]

        ptr['$'] = True

    def search(self, word: str) -> bool:

        def search_inner(word, node):
            for i, ch in enumerate(word):
                if ch not in node:
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_inner(word[i + 1:], node[x]):
                                return True
                    return False
                else:
                    node = node[ch]

            return '$' in node

        return search_inner(word, self.trie)
