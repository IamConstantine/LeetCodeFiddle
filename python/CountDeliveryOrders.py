from functools import cache


# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options
# Hard
# T = O(N**2)
# S = O(N**2)

def countOrders(n: int) -> int:
    mod = 1_000_000_007  # to avoid integer overflow

    @cache
    def permutations(unpicked, undelivered):
        if not unpicked and not undelivered:
            # all orders delivered
            return 1

        if undelivered < 0 or unpicked < 0 or undelivered < unpicked:
            # undelivered can never be less than unpicked
            return 0

        # permutation
        ans = unpicked * permutations(unpicked - 1, undelivered)
        ans %= mod
        ans += (undelivered - unpicked) * permutations(unpicked, undelivered - 1)

        return ans

    return permutations(n, n)
