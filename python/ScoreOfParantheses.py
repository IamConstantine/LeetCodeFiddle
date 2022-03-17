# https://leetcode.com/problems/score-of-parentheses
# Medium
#  T = O(N)
#  S = O(1)

def scoreOfParentheses(s: str) -> int:
    cnt = 0
    bal = 0
    # count the no of cores ie () in sequence
    for i, x in enumerate(s):
        if x == '(':
            bal += 1
        else:
            bal -= 1
            if s[i - 1] == '(':
                cnt += 1 << bal  # raise by power of 2 for each enclosed core
    return cnt
