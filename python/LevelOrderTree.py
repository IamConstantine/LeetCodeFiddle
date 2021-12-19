import collections
from collections import deque
from typing import Optional, List

from Tree import TreeNode


# https://leetcode.com/problems/binary-tree-level-order-traversal
# Medium - easy for me
# For me, Tree questions seems easier.
# T = O(N) - each node exactly once
# S = O(N) - Width of the tree

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    q = deque()
    q.append((0, root))
    l = collections.defaultdict(lambda: [])
    while q:
        level, curr = q.popleft()
        l[level].append(curr.val)
        for node in [curr.left, curr.right]:
            if node:
                q.append((level + 1, node))

    return list(l.values())
