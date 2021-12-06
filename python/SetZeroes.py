from typing import List


# https://leetcode.com/problems/set-matrix-zeroes
# Medium

# My first submission using set for row and column
# T = O(mn)
# S = O(m + n)

def setZeroesFirst(matrix: List[List[int]]):
    zero_rows = set()
    zero_columns = set()

    row = len(matrix)
    column = len(matrix[0])
    for i in range(row):
        for j in range(len(column)):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)

    for i in range(row):
        for j in range(len(column)):
            if i in zero_rows or j in zero_columns:
                matrix[i][j] = 0


# S = O(1) solution by setting flag on the first row and column

def setZeroes(matrix: List[List[int]]):
    row = len(matrix)
    column = len(matrix[0])

    # Since first cell for both first row and first column is the same i.e. matrix[0][0]
    # For this solution we are using an additional variable for the first column
    # and using matrix[0][0] for the first row
    is_col = False

    for i in range(row):  # start from zeroth row
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, column):  # start from 1st column. We will fill zeroth column later
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, row):
        for j in range(1, column):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # setting zeroth row later as the check for flag above would overlap with new values getting set
    # This will cause all values of cell getting if matrix[0][0] is 0

    if matrix[0][0] == 0:  # if there is a zero in first row, it will be denoted by this
        for j in range(column):
            matrix[0][j] = 0

    # setting first column to zero as well
    if is_col:
        for i in range(row):
            matrix[i][0] = 0
