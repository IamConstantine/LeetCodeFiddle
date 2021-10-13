# Better to do it using golden ratio and matrix exponentiation
# https://leetcode.com/problems/fibonacci-number/solution/

def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n

    ans = [0] * (n + 1)
    ans[1] = 1

    for i in range(2, n + 1):
        ans[i] = ans[i - 1] + ans[i - 2]
    return ans[n]
