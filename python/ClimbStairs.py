
# This problem is basically solving fibonacci sequence.Space would be O(1) : dp[i] = dp[i-1] + dp[i-2]
# https://leetcode.com/problems/climbing-stairs

def climbStairs(n):
    def climbStairsInner(n, mem={}):
        if n == 1 or n ==0:
            return 1
        if n < 0:
            return 0
        if n in mem:
            return mem[n]

        n_ways = climbStairsInner(n - 1) + climbStairsInner(n - 2)
        mem[n] = n_ways
        return n_ways

    return climbStairsInner(n)
