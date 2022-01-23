from collections import deque
from typing import Optional

from Tree import TreeNode


# https://leetcode.com/problems/find-nearest-right-node-in-binary-tree
# Medium
# T = O(N) - Visit all nodes once
# S = O(D) - BFS as D is diameter of tree

def findNearestRightNode(root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
    q = deque()
    q.append((root, 0))

    search_level = -1
    while q:
        node, level = q.popleft()
        if node == u:
            search_level = level
        else:
            if level == search_level:
                return node
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

    return None
