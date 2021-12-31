from typing import Optional

from Tree import TreeNode


# https://leetcode.com/problems/kth-smallest-element-in-a-bst
# Medium
# T = O(N)
# S = O(N)

# Follow up: Optimizing kth retrieval if it has frequent modifications
# use a Doubly LL as an index/LRU cache to quickly retrieve the kth element

def kthSmallest_recur(root: Optional[TreeNode], k: int) -> int:
    kthMin = -1

    def inorder(node, index):
        nonlocal kthMin
        if not node:
            return index

        left = inorder(node.left, index)
        if kthMin == -1:
            if left + 1 == k:
                kthMin = node.val
                return 0
        return inorder(node.right, left + 1)

    inorder(root, 0)
    return kthMin


# T = O(N)
# S = O(H) - stack usage. Worst case for skewed tree is N and for balanced case is log N height
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    node = root
    stck = []
    while True:
        while node:
            stck.append(node)
            node = node.left
        curr = stck.pop()
        k -= 1
        if k == 0:
            return curr.val
        node = curr.right
