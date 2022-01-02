from typing import Optional

from Tree import TreeNode


# https://leetcode.com/problems/subtree-of-another-tree
# Easy
# T = O(N * M) - N and M are length of two trees
# S = O(N)
# There's an advanced solution using merkle tree

# Each node of two trees, will maintain merkle hash calculated as hash(merkle of left + val + merkle of right).
# Then just check whether root has merkle of root of subtree
# T = O(N + M) - as you are just doing a regular tree traversal
# https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def findNode(parent, n):
        if not parent:
            return []
        l = [parent] if parent.val == n else []

        return l + findNode(parent.left, n) + findNode(parent.right, n)

    def isSame(node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.val != node2.val:
            return False

        return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)

    subTreeRoots = findNode(root, subRoot.val)
    if not subTreeRoots:
        return False

    for subTreeRoot in subTreeRoots:
        if isSame(subTreeRoot, subRoot):
            return True

    return False
