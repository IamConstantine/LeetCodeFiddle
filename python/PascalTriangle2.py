# https://leetcode.com/problems/pascals-triangle-ii/

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]

    if rowIndex == 1:
        return [1, 1]

    last = [1, 1]

    for row in range(3, rowIndex + 2):
        curr = [1] * row

        for i in range(1, (1 + row) // 2):
            curr[i] = curr[row - 1 - i] = last[i - 1] + last[i]

        last = curr

    return last
