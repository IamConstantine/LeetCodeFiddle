from typing import List


# https://leetcode.com/problems/search-a-2d-matrix-ii
# Medium
# T = O(n + m) as row can only be decremented and column can only be incremented
# S = O(1

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    columns = len(matrix[0])

    row = rows - 1
    col = 0

    while col < columns and row >= 0:
        if target == matrix[row][col]:
            return True

        if target > matrix[row][col]:
            col += 1
        else:
            row -= 1

    return False
