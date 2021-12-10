from typing import Optional

from Tree import TreeNode


# https://leetcode.com/problems/maximum-depth-of-binary-tree#
# Easy

# T = O(N)
# S = O(N) worst case but for BST it can O(logN)

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


def maxDepthBFS(root):
    stack = []
    if root is not None:
        stack.append((1, root))

    depth = 0
    while stack != []:
        current_depth, root = stack.pop()
        if root is not None:
            depth = max(depth, current_depth)
            stack.append((current_depth + 1, root.left))
            stack.append((current_depth + 1, root.right))

    return depth
