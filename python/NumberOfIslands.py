from typing import List


# https://leetcode.com/problems/number-of-islands
# Medium
# T = O(MN)
# S = O(MN)
# can be also solved using Union Find

def numIslands(grid: List[List[str]]) -> int:
    total = 0

    rows = len(grid)
    columns = len(grid[0])

    total_area = sum(1 for x in range(rows) for y in range(columns) if grid[x][y] == '1')

    def map_island(x, y):
        if x == -1 or y == -1 or x == rows or y == columns or grid[x][y] == '0':
            return 0

        grid[x][y] = '0'
        return 1 + map_island(x + 1, y) + map_island(x - 1, y) + map_island(x, y + 1) + map_island(x, y - 1)

    i = 0
    while total_area and i < rows:
        j = 0
        while total_area and j < columns:
            if grid[i][j] == '1':
                total_area -= map_island(i, j)
                total += 1
            j += 1
        i += 1
    return total


# runtime is faster
# a solution that I came up with
def numIslands_unorthodox(grid: List[List[str]]) -> int:
    total = 0

    island_coords = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '1'}

    def map_island(x, y):
        if not island_coords:
            return
        if (x, y) not in island_coords:
            return

        island_coords.remove((x, y))
        map_island(x + 1, y)
        map_island(x - 1, y)
        map_island(x, y + 1)
        map_island(x, y - 1)

    while island_coords:
        p = island_coords.pop()  # runs faster compared to p = next(iter(island_coords))
        island_coords.add(p)
        map_island(*p)
        total += 1

    return total
