# https://leetcode.com/problems/champagne-tower
# Medium
# T = O(R ** 2)
# S = O(R ** 2)

def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    arr = [[0] * (i + 1) for i in range(query_row + 1)]

    arr[0][0] = poured

    for i in range(query_row):  # n - 1
        for j in range(i + 1):
            if arr[i][j] > 1:
                new_poured = arr[i][j] - 1
                arr[i + 1][j] += new_poured / 2
                arr[i + 1][j + 1] += new_poured / 2

    return min(1, arr[query_row][query_glass])  # max capacity of glass is 1
