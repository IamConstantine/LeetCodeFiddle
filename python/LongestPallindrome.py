def longestPalindrome(s: str) -> str:
    res = ''
    for i in range(len(s)):
        res = max(res, findPallindrome(s, i, i), findPallindrome(s, i, i + 1), key=len)

    return res


def findPallindrome(s: str, l, r) -> str:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1: r]
