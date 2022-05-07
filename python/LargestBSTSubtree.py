import math
from typing import Optional

from Tree import TreeNode


# https://leetcode.com/problems/largest-bst-subtree
# Medium
# T = O(N)
# S = O(N)

def largestBSTSubtree(root: Optional[TreeNode]) -> int:
    def inorder(node):
        if not node:
            return 0, math.inf, -math.inf

        l_n, l_min, l_max = inorder(node.left)
        r_n, r_min, r_max = inorder(node.right)

        if l_max < node.val < r_min:
            return 1 + l_n + r_n, min(l_min, node.val), max(r_max, node.val)
        else:
            return max(l_n, r_n), -math.inf, math.inf

    return inorder(root)[0]
