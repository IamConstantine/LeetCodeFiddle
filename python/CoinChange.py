import sys
from typing import List


# https://leetcode.com/problems/coin-change/

# O(S * n) - bottom up approach
def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[amount] == float('inf') else dp[amount]


def coinChange_top(coins: List[int], amount: int) -> int:
    return coinChange_top_helper(coins, amount, [float('inf')] * amount)

def coinChange_top_helper(coins: List[int], rem: int, cnt: List[float]) -> int:
    if rem < 0:
        return -1
    if rem == 0:
        return 0

    if cnt[rem - 1] != float('inf'):
        return int(cnt[rem - 1])
    min_cnt = sys.maxsize
    for coin in coins:
        res = coinChange_top_helper(coins, rem - coin, cnt)
        if 0 <= res < min_cnt:
            min_cnt = res + 1
    cnt[rem - 1] = min_cnt if min_cnt != sys.maxsize else -1
    return cnt[rem - 1]
