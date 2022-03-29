import heapq
from typing import List


# https://leetcode.com/problems/path-with-maximum-minimum-value
# Medium
# T = O(R*C * log(R * C)) - log(R * C) - required for heap push and pop
# S = O(R * C)

# The solution focuses on traversing from 0,0 by choosing max value from neighbour everytime.
# We will use a max heap to always traverse to max yielding path

def maximumMinimumPath(grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])

    # 4 directions to a cell's possible neighbors.
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[False] * C for _ in range(R)]

    heap = []
    ans = grid[0][0]

    # Put the top-left cell to the priority queue and mark it as True (visited).
    # Notice that we save the negative number of cell's value, thus we can always
    # pop out the cell with the maximum value using a min-heap data structure.
    heapq.heappush(heap, (-ans, 0, 0))
    visited[0][0] = True

    while heap:
        curr_val, curr_row, curr_col = heapq.heappop(heap)
        ans = min(ans, grid[curr_row][curr_col])

        if curr_row == R - 1 and curr_col == C - 1:
            break
        for d_row, d_col in dirs:
            new_row = curr_row + d_row
            new_col = curr_col + d_col

            if 0 <= new_row < R and 0 <= new_col < C and not visited[new_row][new_col]:
                heapq.heappush(heap, (-grid[new_row][new_col], new_row, new_col))
                visited[new_row][new_col] = True

    return ans
