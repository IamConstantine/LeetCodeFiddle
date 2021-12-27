from collections import deque


# https://leetcode.com/problems/clone-graph
# Medium
# T = O(V + E) - For BFS/DFS
# S = O(N) - For the dict

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def cloneGraph(node: Node) -> Node:
    if not node:
        return node
    new = Node(node.val)
    visited = {1: new}

    q = deque()
    q.append(node)

    while q:
        n = q.popleft()
        for x in n.neighbors:
            if x.val not in visited:
                visited[x.val] = Node(x.val)
                q.append(x)
            visited[n.val].neighbors.append(visited[x.val])

    return new


# Adjacency list is index + 1. So the first element of adjacency_list are neighbors for Node 1
def buildNodeGraph(adjacency_list):
    if not adjacency_list:
        return None
    node = Node(1)
    n = {1: node}

    for i, (x, y) in enumerate(adjacency_list):
        if x not in n:
            n[x] = Node(x)
        if y not in n:
            n[y] = Node(y)

        n[i + 1].neighbors.append(n[x])
        n[i + 1].neighbors.append(n[y])
    return node


def buildAdjacencyList(node: Node):
    if not node:
        return []
    q = deque()
    q.append(node)

    n = {1: []}  # first node's value is 1

    while q:
        popped = q.popleft()
        for x in popped.neighbors:
            if x.val not in n:
                n[x.val] = []
                q.append(x)
            n[popped.val].append(x.val)

    adjacency_list = [None] * len(n)
    for i in range(1, len(n) + 1):
        adjacency_list[i - 1] = n[i]
    return adjacency_list
