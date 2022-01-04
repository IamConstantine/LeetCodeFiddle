# https://leetcode.com/problems/implement-trie-prefix-tree/solution/
# Medium
# T, S
# insert = O(m), O(m)
# search = O(m), O(1)
# startsWith = O(m), O(1)

class TrieNode:
    def __init__(self):
        # can be replaced with children dict which maintains char,node tuple
        self.children = {}  # all lowercase chars
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.isEndOfWord = True
        return node.isEndOfWord

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return node.isEndOfWord

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


obj = Trie()
word = 'apple'
obj.insert(word)
print(obj.search(word))
print(obj.startsWith('app'))
