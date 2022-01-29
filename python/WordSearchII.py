from typing import List


# https://leetcode.com/problems/word-search-ii
# Hard
# T = O(M(4*3**L-1)) - M is no of cells in board. Root node has 4 options and then each option has 3^L-1
# S = O(N)

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    trie = {}

    # The Trie implementation was my own and was same as LC author solution
    for word in words:
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node['$'] = word

    def get_coords(p, q):
        return [(x, y) for x, y in [(p + 1, q), (p - 1, q), (p, q + 1), (p, q - 1)] if
                -1 < x < len(board) and -1 < y < len(board[0])]

    found = []

    def search(x, y, parent):
        letter = board[x][y]
        curr = parent[board[x][y]]

        if '$' in curr:
            found.append(curr.pop('$'))

        board[x][y] = '#'
        for p, q in get_coords(x, y):
            if board[p][q] in curr:
                search(p, q, curr)

        board[x][y] = letter

        if not curr:  # will be a leaf node if we pop the '$'
            parent.pop(letter)

    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] in trie:
                search(row, column, trie)

    return found
