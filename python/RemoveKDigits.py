# https://leetcode.com/problems/remove-k-digits
# Medium
# T = O(N) - there is an inner loop which will run k times. So its O(N + k) times
# S = O(N)

def removeKdigits(num: str, k: int) -> str:
    stck = []

    for d in num:
        while k and stck and stck[-1] > d:
            stck.pop()
            k -= 1

        stck.append(d)

    res = stck[:-k] if k else stck
    return ''.join(res).lstrip('0') or '0'
