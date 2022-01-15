from typing import List


# https://leetcode.com/problems/pacific-atlantic-water-flow
# Medium
# T = O(M * N) ~ O(2 * M * N) - worst case both atlantic and pacific visit all cells ie. all are equal in height
# S = O(M * N)

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    row = len(heights)
    column = len(heights[0])

    def dfs(x, y, visited):
        if (x, y) in visited:
            return
        stack = [(x, y)]
        visited.add((x, y))
        while stack:
            r, c = stack.pop()
            curr_height = heights[r][c]
            for p, q in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                if 0 <= p < row and 0 <= q < column and (p, q) not in visited and heights[p][q] >= curr_height:
                    stack.append((p, q))
                    visited.add((p, q))

    pacific = set()
    atlantic = set()

    for i in range(row):
        dfs(i, 0, pacific)
        dfs(i, column - 1, atlantic)

    for i in range(column):
        dfs(0, i, pacific)
        dfs(row - 1, i, atlantic)

    return list(pacific.intersection(atlantic))
