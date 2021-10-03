import sys
from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices: List[int]) -> int:
    profit = 0
    buy_amount = sys.maxsize
    for i in range(len(prices)):
        if buy_amount > prices[i]:
            buy_amount = prices[i]
        elif buy_amount < prices[i]:
            profit = max(profit, prices[i] - buy_amount)
    return profit
