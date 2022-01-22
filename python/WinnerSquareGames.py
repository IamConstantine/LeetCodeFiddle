from functools import lru_cache


# https://leetcode.com/problems/stone-game-iv
# Hard
# T = O(N * sqr_root(N))
# T = O(N) - for recursion with caching. Without caching it would be - O(N * sqr_root(N))
def winnerSquareGame_dfs(n: int) -> bool:
    @lru_cache(maxsize=None)
    def dfs(rem):
        if rem == 0:
            return False

        sqr_root = int(rem ** 0.5)
        for i in range(1, sqr_root + 1):  # a player can subtract upto square root stones
            if not dfs(rem - i * i):
                return True
        return False

    return dfs(n)


def winnerSquareGame(n: int) -> bool:
    dp = [False] * (n + 1)
    for i in range(1, n + 1):  # calculating for each n
        for k in reversed(range(1, int(i ** 0.5) + 1)):
            if not dp[i - k * k]:
                dp[i] = True
                break
    return dp[n]
