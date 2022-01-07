from functools import lru_cache


# https://leetcode.com/problems/longest-common-subsequence
# Medium

# Intuitive
# T = O(M * N^2) - M * N possible combinations for
# two indices and for each combination we traverse N times for finding the character.
# S = O(M * N)

def longestCommonSubsequence_intuitive(text1: str, text2: str) -> int:
    @lru_cache(maxsize=None)  # for unbounded caching
    def longestCommonSubsequenceInner(idx1, idx2):
        if idx1 == len(text1) or idx2 == len(text2):
            return 0

        case1 = longestCommonSubsequenceInner(idx1 + 1, idx2)

        case2 = 0
        first_occurrence = text2.find(text1[idx1], idx2)
        if first_occurrence != -1:
            case2 = 1 + longestCommonSubsequenceInner(idx1 + 1, first_occurrence + 1)
        return max(case1, case2)

    return longestCommonSubsequenceInner(0, 0)


# Intuitive
# T = O(M * N) - Got rid of the find char loop. In above solution, if case2 happens, its always max
# S = O(M * N)

def longestCommonSubsequenceSmarter(text1: str, text2: str) -> int:
    @lru_cache(maxsize=None)  # for unbounded caching
    def longestCommonSubsequenceInner(idx1, idx2):
        if idx1 == len(text1) or idx2 == len(text2):
            return 0

        if text1[idx1] == text2[idx2]:
            return 1 + longestCommonSubsequenceInner(idx1 + 1, idx2 + 1)
        else:
            return max(longestCommonSubsequenceInner(idx1 + 1, idx2), longestCommonSubsequenceInner(idx1, idx2 + 1))

    return longestCommonSubsequenceInner(0, 0)


# DP bottom up
# T = O(M * N)
# S = O(M * N)

def longestCommonSubsequenceDP(text1: str, text2: str):
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    for col in reversed(range(len(text2))):
        for row in reversed(range(len(text1))):
            if text1[row] == text2[col]:
                dp[row][col] = 1 + dp[row + 1][col + 1]  # 1 + next char(idx1 + 1, idx2 + 1 )
            else:
                dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])

    return dp[0][0]


# DP bottom up
# T = O(M * N)
# S = O(min(M ,N))

def longestCommonSubsequence(text1: str, text2: str):
    # find min length
    if len(text2) < len(text1):
        text1, text2 = text2, text1

    prev = [0] * (len(text1) + 1)

    for col in reversed(range(len(text2))):
        curr = [0] * (len(text1) + 1)
        for row in reversed(range(len(text1))):
            if text1[row] == text2[col]:
                curr[row] = 1 + prev[row + 1]
            else:
                curr[row] = max(curr[row + 1], prev[row])
        prev = curr
    return prev[0]
