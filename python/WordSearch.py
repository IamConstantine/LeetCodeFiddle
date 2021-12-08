from typing import List


# https://leetcode.com/problems/word-search
# Medium

# T = O(N.3^L) - N is no of cells and 3 is the directions we explore and L is the length of word
# S = O(N + L) - N is visited matrix and L is the recursion depth

def exist(board: List[List[str]], word: str) -> bool:
    rows = len(board)
    columns = len(board[0])
    visited = [[0] * columns for _ in range(rows)]

    word_length = len(word)

    def existInner(s, m, n):
        if s == word_length:
            return True
        if m == rows or n == columns or m < 0 or n < 0:
            return False
        if visited[m][n]:
            return False
        if word[s] != board[m][n]:
            return False

        visited[m][n] = 1
        hasSeq = existInner(s + 1, m + 1, n) or existInner(s + 1, m - 1, n) or existInner(s + 1, m,
                                                                                          n + 1) or existInner(s + 1, m,
                                                                                                               n - 1)
        if hasSeq:
            return True
        visited[m][n] = 0
        return False

    for x in range(rows):
        for y in range(columns):
            if word[0] == board[x][y]:
                if existInner(0, x, y):
                    return True

    return False
