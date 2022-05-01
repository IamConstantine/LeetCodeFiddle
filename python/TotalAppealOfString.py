# https://leetcode.com/problems/total-appeal-of-a-string
# Hard
# T = O(N)
# S = O(1) - as the char set is all lowercase characters

def appealSum(s: str) -> int:
    lastSeenMap = {s[0]: 0}
    prev, curr, res = 1, 0, 1

    for i in range(1, len(s)):
        if s[i] in lastSeenMap:
            curr = prev + (i - lastSeenMap[s[i]])
        else:
            curr = prev + (i + 1)
        res += curr
        prev = curr
        lastSeenMap[s[i]] = i
    return res
