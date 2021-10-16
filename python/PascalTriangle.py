from typing import List


def generate(numRows: int) -> List[List[int]]:
    result = [[1]]
    for row in range(2, numRows + 1):
        curr = [1] * row
        i = 1
        j = (1 + row) // 2
        while i < j:
            last = result[-1]
            curr[i] = curr[row - 1 - i] = last[i - 1] + last[i]
            i += 1
        result.append(curr)
    return result
