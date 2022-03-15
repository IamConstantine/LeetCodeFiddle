from collections import defaultdict


# https://leetcode.com/problems/longest-repeating-character-replacement
# Medium
# T = O(N)
# S = O(N)
# The problem statement on website is vague as of 15th March 2022.
# The list of chars can be replaced from any Character to any character k times.

# Sliding Window
def characterReplacement(s: str, k: int) -> int:
    longest = 0
    left = 0

    # store the freq of chars in a valid window
    freq = defaultdict(int)

    for right in range(len(s)):
        freq[s[right]] += 1

        # length of window - top char count should be less than k
        # It's just to find minimum no of deletions needed to make
        # window made of same chars
        if right - left + 1 - max(freq.values()) <= k:
            longest = max(longest, right - left + 1)
        else:
            # shrink the window from the left if its invalid
            freq[s[left]] -= 1

            if not freq[s[left]]:
                del freq[s[left]]

            left += 1

    return longest
