# https://leetcode.com/problems/unique-paths
# Medium

# T = O(mn)
# S = O(mn)

def uniquePaths(m: int, n: int) -> int:
    # mem = ([[0] * n] * m) # this always meeses up as I am copying the same array m times

    mem = [[1] * n for _ in range(m)]

    for r in range(1, m):
        for c in range(1, n):
            mem[r][c] = mem[r - 1][c] + mem[r][c - 1]

    return mem[m - 1][n - 1]


# a recursive approach and a starting point to figure out the DP approach

def uniquePathsBrute(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1

    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)


# recursive with memoisation

def uniquePathsRecur(m: int, n: int) -> int:
    mem = [[0] * n for _ in range(m)]

    def uniquePathsRecurInner(r, c):
        if r == m - 1 or c == n - 1:
            mem[r][c] = 1
            return 1

        if mem[r][c] != 0:
            return mem[r][c]

        mem[r][c] = uniquePathsRecurInner(r + 1, c) + uniquePathsRecurInner(r, c + 1)
        return mem[r][c]

    return uniquePathsRecurInner(0, 0)
