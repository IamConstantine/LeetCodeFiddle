from typing import List

# https://leetcode.com/problems/min-cost-climbing-stairs

def minCostClimbingStairs(cost: List[int]) -> int:
    dp = [-1] * len(cost)

    def minCostClimbingStairsInner(start, length):
        if length - 1 <= start:
            return 0
        if dp[start] != -1:
            return dp[start]

        min_value = min(cost[start] + minCostClimbingStairsInner(start + 1, length),
                        cost[start + 1] + minCostClimbingStairsInner(start + 2, length))
        dp[start] = min_value
        return min_value

    return minCostClimbingStairsInner(0, len(cost))

def minCostClimbingStairs_bottom_up(cost: List[int]) -> int:
    # The array's length should be 1 longer than the length of cost
    # This is because we can treat the "top floor" as a step to reach
    minimum_cost = [0] * (len(cost) + 1)

    # Start iteration from step 2, since the minimum cost of reaching
    # step 0 and step 1 is 0
    for i in range(2, len(cost) + 1):
        # to reach i, which is the min route
        take_one_step = minimum_cost[i - 1] + cost[i - 1]
        take_two_steps = minimum_cost[i - 2] + cost[i - 2]
        minimum_cost[i] = min(take_one_step, take_two_steps)

    # The final element in minimum_cost refers to the top floor
    return minimum_cost[-1]


# fastest one
def minCostClimbingStairs_withConstantSpace(cost: List[int]) -> int:
    down_one = down_two = 0
    for i in range(2, len(cost) + 1):
        temp = down_one
        down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
        down_two = temp

    return down_one

def minCostClimbingStairs_withoutDp(cost: List[int]) -> int:

    def minCostClimbingStairsInner(start, length):
        if length - 1 <= start:
            return 0
        return min(cost[start] + minCostClimbingStairsInner(start + 1, length),
                   cost[start + 1] + minCostClimbingStairsInner(start + 2, length))

    return minCostClimbingStairsInner(0, len(cost))
