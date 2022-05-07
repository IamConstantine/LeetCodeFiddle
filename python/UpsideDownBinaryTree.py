from typing import Optional

from Tree import TreeNode


# https://leetcode.com/problems/binary-tree-upside-down
# Medium
# T = O(N)
# S = O(1)

def upsideDownBinaryTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    prev = leaf = None
    curr = root

    while curr:
        curr.right, curr.left, curr, prev, leaf = prev, leaf, curr.left, curr, curr.right

    return prev
