# https://leetcode.com/problems/decode-ways
# Nedium

# T = O(N)
# S = O(N) can be O(1) -  You dont need a DP array as you are looking back only max i-2 values which is similar to Fibonacci

# I had tried to solve it using dp. Figured it was a DP problem after some analysis and wasn't able to deliver the solution
# as I was playing with wrong conditions
# The major thing that I missed. I was doing 0 <= 2_digit <=26 which made me handle an extra if
# You dont need a DP array as you are looking back only max i-2 values which is similar to Fibonacci

def numDecodings(s: str) -> int:
    if s[0] == '0':
        return 0

    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, len(dp)):
        if s[i - 1] != '0':
            dp[i] = dp[i - 1]

        if 10 <= int(s[
                     i - 2: i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[-1]
