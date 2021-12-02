from typing import List


# https://leetcode.com/problems/spiral-matrix
# Medium
# A Simple problem - But the time taken is to figure out the directions, boundaries and edge cases
# Time = O(M.N) and Space = O(1) as output array is ignored

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    row = len(matrix)
    column = len(matrix[0])

    l = []

    left = up = 0
    down = row - 1
    right = column - 1

    while len(l) != (row * column):
        for i in range(left, right + 1):
            l.append(matrix[up][i])

        for i in range(up + 1, down + 1):
            l.append(matrix[i][right])

        if up != down:  # As its the same row, dont go left as we already went right on the same row
            for i in range(right - 1, left - 1, -1):
                l.append(matrix[down][i])

        if left != right: # As its the same column, dont go up as we already went down on the same column
            for i in range(down - 1, up, -1):
                l.append(matrix[i][left])

        right -= 1
        down -= 1
        left += 1
        up += 1

    return l
