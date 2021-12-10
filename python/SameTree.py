from typing import Optional

from Tree import TreeNode

# https://leetcode.com/problems/same-tree
# Super Easy

# T = O(n)
# S = O(N) worst case but for BST it can O(logN)

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if (not p and q) or (not q and p):
        return False

    return (not p and not q) or (p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right))
