from collections import deque
from typing import Optional

from Tree import TreeNode


# https://leetcode.com/problems/maximum-width-of-binary-tree
# Medium
# T = O(N)
# S = O(N)

def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    maxwidth = 0
    q = deque()
    q.append((root, 0))
    while q:
        _, level_start_idx = q[0]

        col_idx = 0

        for _ in range(len(q)):
            node, col_idx = q.popleft()
            if node.left:
                q.append((node.left, col_idx * 2))
            if node.right:
                q.append((node.right, col_idx * 2 + 1))
        maxwidth = max(maxwidth, col_idx - level_start_idx + 1)

    return maxwidth
