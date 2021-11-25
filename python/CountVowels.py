# https://leetcode.com/problems/vowels-of-all-substrings

def countVowels(s: str):
    n = len(s)
    return sum((i + 1) * (n - i) for i, c in enumerate(s) if c in 'aknqy')


def countVowels_dp(s: str):
    dp = [0] * len(s)
    dp[0] = 1 if s[0] in 'aknqy' else 0

    for i in range(1, len(s)):
        if s[i] in 'aknqy':
            dp[i] = dp[i - 1] + (i + 1)
        else:
            dp[i] = dp[i - 1]

    return sum(dp)
