from typing import List, Optional
from collections import defaultdict, deque
from Tree import TreeNode


# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal Medium T = O(N) - each
# element visited once and O(1) lookups for index. S = O(N) - for hash map.

# The problem defines distinct node values.
# If there were duplicates, its possible to have more than one tree. In that case, we need a list of node refs for
# inorder and preorder instead of values.

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def buildTreeInner(l, r):  # l, r are used as a way to track the size of subtree. Size of subtree - r - l + 1.
        nonlocal preorder_index
        if l > r:  # no elements for this subtree. So return
            return None
        node = TreeNode(preorder[preorder_index])
        index = inorder_map[preorder[preorder_index]]

        preorder_index += 1

        node.left = buildTreeInner(l, index - 1)
        node.right = buildTreeInner(index + 1, r)
        return node

    preorder_index = 0
    inorder_map = defaultdict(int)
    for i, element in enumerate(inorder):
        inorder_map[element] = i
    return buildTreeInner(0, len(inorder) - 1)


# get rid of hashmap
# We are using inorder to track if we consumed all and we dont care of what we are popping.
# we bound left subtree using parent value an right is unbounded.
# These help us define the termination condition for the recursion.

def buildTreeSmarter(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    preorder = deque(preorder)
    inorder = deque(inorder)

    def helper(bound=None):
        if not inorder or inorder[0] == bound:
            return None
        root = TreeNode(preorder.popleft())
        root.left = helper(root.val)
        inorder.popleft()
        root.right = helper(bound)
        return root

    return helper()
