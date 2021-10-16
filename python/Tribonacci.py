# https://leetcode.com/problems/n-th-tribonacci-number/

def tribonacci(n: int):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    nMinusThree = 0
    nMinusTwo = 1
    nMinusOne = 1
    result = 0
    for i in range(3, n + 1):
        result = nMinusThree + nMinusTwo + nMinusOne
        nMinusThree, nMinusTwo, nMinusOne = (nMinusTwo, nMinusOne, result)

    return result


def tribonacci_dp(n: int):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1

    for i in range(3, len(dp)):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]
