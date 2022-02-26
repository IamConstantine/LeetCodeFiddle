# https://leetcode.com/problems/shortest-path-visiting-all-nodes
# Hard
# T = O(2**N * N ** 2) - 2 ** N - possible mask combinations,
# n ** 2 - worst case eeach node is connected to all other nodes
#
# S = O(2 ** N * N)

def shortestPathLength(graph):
    n = len(graph)
    cache = {}
    ending_mask = (1 << n) - 1  # acts as visited bit map

    def dp(node, mask):
        state = (node, mask)

        if state in cache:
            return cache[state]

        # termination condition
        if mask & (mask - 1) == 0:  # only 1 bit is set
            return 0

        cache[state] = float('inf')

        for neighbour in graph[node]:
            if mask & (1 << neighbour):
                not_visited = 1 + dp(neighbour, mask)  # dont mark visited, as we are allowed to revisit multiple times
                visited = 1 + dp(neighbour, mask ^ (1 << node))
                cache[state] = min(cache[state], visited, not_visited)
        return cache[state]

    return min(dp(x, ending_mask) for x in range(n))
