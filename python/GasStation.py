from typing import List


# https://leetcode.com/problems/gas-station
# Medium
# T = O(N)
# S = O(1)

# Unintuitive
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    tot_gas, curr_gas = 0, 0
    start = 0
    for i in range(len(gas)):
        tot_gas += gas[i] - cost[i]
        curr_gas += gas[i] - cost[i]
        if curr_gas < 0:
            curr_gas = 0
            start = i + 1

    return -1 if tot_gas < 0 else start
