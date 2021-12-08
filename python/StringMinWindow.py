import collections
from collections import Counter


# https://leetcode.com/problems/minimum-window-substring
# Hard

# T = O(S + T), S = len of s and T = len of t. It would be O(2S + T) for worst as left and right would scan each char of s twice.
# S = O(S + T), S is the window size and T is the unique chars of T


def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ''

    dict_t = Counter(t)  # count of chars in t

    required = len(dict_t)  # count of unique chars in t

    formed = 0  # count of unique chars in window. eg: t = 'AABC' and window all 4, then formed = 3. if window has only 'ABC', then formed = 2

    ans = float("inf"), None, None
    l, r = 0, 0

    window = collections.defaultdict(int)

    while r < len(s):
        character = s[r]
        window[character] += 1
        if window[character] == dict_t[character]:
            formed += 1

        # if formed = required, it means the current window is valid. So start moving l until its valid
        while l <= r and formed == required:
            if r - l + 1 < ans[0]:
                ans = r - l + 1, l, r

            character = s[l]
            window[character] -= 1

            if window[character] < dict_t[character]:
                formed -= 1
            l += 1
        r += 1

    return '' if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


# there is a solution using filtered_s approach which reduced T Significantly when there too many invalid chars in s
# The worst T here is 2 * filtered_s + S + T

def minWindowWithFilteredS(s: str, t: str) -> str:
    if not s or not t:
        return ''

    dict_t = Counter(t)  # count of chars in t
    required = len(dict_t)  # count of unique chars in t

    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))  # add only t chars

    formed = 0  # count of unique chars in window. eg: t = 'AABC' and window all 4, then formed = 3. if window has only 'ABC', then formed = 2

    ans = float("inf"), None, None
    l, r = 0, 0

    window = collections.defaultdict(int)

    while r < len(filtered_s):
        character = filtered_s[r][1]
        window[character] += 1
        if window[character] == dict_t[character]:
            formed += 1

        # if formed = required, it means the current window is valid. So start moving l until its valid
        while l <= r and formed == required:
            start = filtered_s[l][0]
            end = filtered_s[r][0]
            if end - start + 1 < ans[0]:
                ans = end - start + 1, start, end

            character = filtered_s[l][1]
            window[character] -= 1

            if window[character] < dict_t[character]:
                formed -= 1
            l += 1
        r += 1

    return '' if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


# least complex solution using just a dict_t and t count

def minWindowLessComplex(s: str, t: str) -> str:
    if not s or not t:
        return ''

    dict_t = Counter(t)  # count of chars in t

    target = len(t)
    ans = float('inf'), None, None
    l = r = 0
    while r < len(s):
        target -= dict_t[s[r]] > 0
        dict_t[s[r]] -= 1
        while target == 0:
            if r - l + 1 < ans[0]:
                ans = r - l + 1, l, r
            target += dict_t[s[l]] >= 0
            dict_t[s[l]] += 1
            l += 1
        r += 1

    return '' if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
