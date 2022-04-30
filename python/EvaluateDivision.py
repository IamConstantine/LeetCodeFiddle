from collections import defaultdict
from typing import List

# https://leetcode.com/problems/evaluate-division
# Medium
# T = O(M.N) - M is number of queries and N is the number of equations
# S = O(N) - store all equations i.e. adjacency list

adj_list = defaultdict(lambda: defaultdict(float))


def backtrack_calculate(curr_node, target_node, acc, visited):
    visited.add(curr_node)
    neighbors = adj_list[curr_node]
    res = -1.0
    if target_node in neighbors:
        res = acc * neighbors[target_node]
    else:
        for neighbor, value in neighbors.items():
            if neighbor not in visited:
                res = backtrack_calculate(neighbor, target_node, acc * value, visited)
                if res != -1.0:
                    break
    visited.remove(curr_node)
    return res


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    for (dividend, divisor), value in zip(equations, values):
        # add nodes and two edges into the graph
        adj_list[dividend][divisor] = value
        adj_list[divisor][dividend] = 1 / value

    res = []
    for dividend, divisor in queries:
        if dividend not in adj_list or divisor not in adj_list:
            res.append(-1.0)
        elif dividend == divisor:
            res.append(1.0)
        else:
            res.append(backtrack_calculate(dividend, divisor, 1.0, set()))

    return res
