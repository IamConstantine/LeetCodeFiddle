import collections
from typing import List


# https://leetcode.com/problems/word-search-ii/
# Hard





def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    rows = len(board)
    columns = len(board[0])

    mem = collections.defaultdict(lambda: {})

    char_indices = collections.defaultdict(lambda: [])
    for x in range(rows):
        for y in range(columns):
            char_indices[board[x][y]].append((x, y))

    def findWordsInner(word, start, x, y, visited):
        if x == -1 or y == -1 or x == rows or y == columns:
            return False

        if (x, y) in mem and word[start:] in mem[(x, y)]:
            return mem[(x, y)][word[start:]]

        if (x, y) in visited:
            return False
        if board[x][y] != word[start]:
            return False
        if start == len(word) - 1:
            return True
        visited.add((x, y))

        start = start + 1
        found = findWordsInner(word, start, x + 1, y, visited) or findWordsInner(word, start, x, y + 1,
                                                                                 visited) or findWordsInner(
            word, start, x - 1, y, visited) or findWordsInner(word, start, x, y - 1, visited)

        mem[(x, y)][word[start:]] = found
        return found

    output = []
    for word in words:
        for x, y in char_indices[word[0]]:
            if findWordsInner(word, 0, x, y, set()):
                output.append(word)
                break
    return output
