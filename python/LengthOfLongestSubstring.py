# https://leetcode.com/explore/interview/card/google/59/array-and-strings/3047/

def lengthOfLongestSubstring(s: str) -> int:
    dict = {}
    max_total = 0
    cnt = 0
    i = 0
    for j in range(len(s)):
        if s[j] in dict and dict[s[j]] >= i:
            i = dict[s[j]] + 1
            max_total = max(max_total, cnt)
            cnt = j - i
        dict[s[j]] = j
        cnt += 1
    return max_total
