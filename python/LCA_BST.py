from Tree import TreeNode


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
# Easy
# T + O(N)
# S = O(1)

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    node = root

    while node:
        value = node.val
        if p.val > value and q.val > value:
            node = node.right
        elif p.val < value and q.val < value:
            node = node.left
        else:
            return node
