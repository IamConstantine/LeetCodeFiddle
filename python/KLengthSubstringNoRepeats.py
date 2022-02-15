from collections import defaultdict


# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters
# Medium
# T = O(n) - length of string - each char is visited atmost twice
# S = O(m) - length of window. If the chars are in a specific set, it can be considered O(1).

def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    if k > len(s):
        return 0

    cnt = 0

    left = right = 0
    freq = defaultdict(int)

    while right < len(s):
        freq[s[right]] += 1

        while freq[s[right]] > 1:  # will never cross right as it will stop when freq == 1
            freq[s[left]] -= 1
            left += 1

        if right - left + 1 == k:
            freq[s[left]] -= 1
            cnt += 1
            left += 1

        right += 1

    return cnt
