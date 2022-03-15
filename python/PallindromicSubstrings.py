# https://leetcode.com/problems/palindromic-substrings
# Medium
# T = O(N**2) - for each center we can expand to N length if all chars in string s are same.
# S = O(1)

def countSubstrings(s: str) -> int:
    length_of_s = len(s)

    def expandAndCountAroundCenter(low, high):
        cnt = 0
        while low >= 0 and high < length_of_s and s[low] == s[high]:
            low -= 1
            high += 1
            cnt += 1
        return cnt

    ans = 0
    for i in range(length_of_s):
        ans += expandAndCountAroundCenter(i, i)  # for odd length pallindrome
        ans += expandAndCountAroundCenter(i, i + 1)  # for even length pallindrome

    return ans
