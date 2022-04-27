from collections import defaultdict
from typing import List


# https://leetcode.com/problems/smallest-string-with-swaps
# Medium

# T = E(adjacency list) + (E + V)(DFS) + VLogV(sort) - O(E + VlogV)
# S = E + V

def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    n = len(s)
    adj_list = defaultdict(list)

    for x, y in pairs:
        adj_list[x].append(y)
        adj_list[y].append(x)

    visited = [False] * n

    def dfs(node, indices, chars):
        indices.append(node)
        chars.append(s[node])
        visited[node] = True
        for next_node in adj_list[node]:
            if not visited[next_node]:
                dfs(next_node, indices, chars)

    ans = [None] * n
    for i in range(n):
        if not visited[i]:
            indices = []
            chars = []
            dfs(i, indices, chars)

            indices.sort()
            chars.sort()
            for i in range(len(indices)):
                ans[indices[i]] = chars[i]

    return ''.join(ans)
