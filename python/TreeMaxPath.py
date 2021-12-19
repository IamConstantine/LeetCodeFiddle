from typing import Optional

from Tree import TreeNode


# https://leetcode.com/problems/binary-tree-maximum-path-sum
# Hard
# Solved it in like half an hour. Proud moment :)
# T = O(N) - each element visited once
# S = O(N) or O(H) - Worst case or O(log N) if a balanced tree

def maxPathSum(root: Optional[TreeNode]) -> int:
    max_sum = -float('inf')

    def maxPathInner(node):
        nonlocal max_sum
        if not node:
            return 0

        left = maxPathInner(node.left)
        right = maxPathInner(node.right)

        max_sum = max(node.val + max(left, right), node.val + right + left, max_sum, node.val)
        return max(node.val + max(left, right), node.val)

    maxPathInner(root)
    return max_sum


# Below code has same complexity but it makes it more concise
def maxPathSumLC(root: Optional[TreeNode]) -> int:
    max_sum = -float('inf')

    def maxPathInner(node):
        nonlocal max_sum
        if not node:
            return 0

        left = max(maxPathInner(node.left), 0)  # its required to get rid of neg gain when we return to parent
        right = max(maxPathInner(node.right), 0)

        max_sum = max(max_sum, node.val + right + left)
        return node.val + max(left, right)

    maxPathInner(root)
    return max_sum
