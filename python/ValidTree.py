import collections
from typing import List


# https://leetcode.com/problems/graph-valid-tree
# Medium
# T = O(V + E) - adjacency list creation
# S = O(V + E) - adjacency list ¬

def validTree_complex(n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:  # in case of tree, its n-1
        return False
    adjacency_list = collections.defaultdict(lambda: [])
    for x, y in edges:
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

    parent = {0: -1}
    stck = [0]
    while stck:
        popped = stck.pop()
        for x in adjacency_list[popped]:
            if x == parent[popped]:
                continue
            if x in parent:  # if for the neighbour, a parent is already defined
                return False
            parent[x] = popped
            stck.append(x)

    return len(parent) == n  # disconnected components after one 1 BFS traversal


# T = O(N) - As O(V + E) = O(V + V - 1) = O(V)
# S = O(N) - we construct adjacency list only if its tree

def validTree(n: int, edges: List[List[int]]):
    if len(edges) != n - 1:  # if doesn't match this, then its not a tree
        return False

    # rest of the code is to check if all the nodes are connected
    adj_list = [[] for _ in range(n)]

    for x, y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)

    stck = [0]
    visited = set()
    while stck:
        popped = stck.pop()
        visited.add(popped)
        for x in adj_list[popped]:
            if x not in visited:
                stck.append(x)

    return len(visited) == n
