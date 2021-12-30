import collections
from collections import deque
from typing import List


# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph
# Medium
# T = O(V + E)
# S = O(V + E) - to build adjacency list, we need E space
# There's a union find solution which takes only O(V) space

def countComponents(n: int, edges: List[List[int]]) -> int:
    nodes = {x for x in range(n)}

    cnt = 0
    adj = collections.defaultdict(lambda: set())

    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)

    while nodes:
        n = nodes.pop()
        nodes.add(n)

        # BFS
        q = deque()
        q.append(n)
        while q:
            popped = q.pop()
            if popped in nodes:
                nodes.remove(popped)
                for x in adj[popped]:
                    if x in nodes:
                        q.append(x)
        cnt += 1
    return cnt

