import math
from typing import Optional

from Tree import TreeNode


# https://leetcode.com/problems/validate-binary-search-tree
# Medium
# T = S = O(N)

# My Solution without Hint - Its bottom up approach using Postorder Traversal
def isValidBST(root: Optional[TreeNode]) -> bool:
    def isValidBSTInner(node):
        if not node.left and not node.right:
            return True, node.val, node.val

        left = isValidBSTInner(node.left) if node.left else (True, float('inf'), -float('inf'))
        right = isValidBSTInner(node.right) if node.right else (True, float('inf'), -float('inf'))

        if left[0] and right[0] and left[2] < node.val < right[
            1]:  # check if node is bigger than max of left and smaller than min of right
            return True, node.val if left[1] == float('inf') else left[1], node.val if right[2] == -float('inf') else \
                right[2]
        return False, float('inf'), -float('inf')

    return isValidBSTInner(root)[0]


# LC solution
def isValidBSTPreorder(root: TreeNode) -> bool:
    def validate(node, low: object = -math.inf, high=math.inf):
        # Empty trees are valid BSTs.
        if not node:
            return True
        # The current node's value must be between low and high.
        if node.val <= low or node.val >= high:
            return False

        # The left and right subtree must also be valid.
        return (validate(node.right, node.val, high) and
                validate(node.left, low, node.val))

    return validate(root)
