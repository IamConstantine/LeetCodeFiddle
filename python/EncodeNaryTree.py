from collections import deque
from typing import Optional


# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree
# Hard
# T = O(N)
# S = O(N) - queue used for BFS traversal

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# The Binary tree representation of an N-ary tree is as follows:
# The left child of a node would hold all the children. The left child would act as a head of the Linked list of its
# children. The next nodes in Linked List are connected using right pointers. The right child of a node is a Linked
# list of all the its siblings. The root node has no sibling and hence no right child

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None

        new_root = TreeNode(root.val)
        q = deque()
        q.append((root, new_root))
        while q:
            old, new = q.popleft()
            head = TreeNode(-1)
            curr = head
            for child in old.children:
                node = TreeNode(child.val)
                curr.right = node
                curr = curr.right
                q.append((child, node))
            new.left = head.right

        return new_root

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None

        new_node = Node(data.val, [])
        if data.left:
            temp = data.left
            while temp:
                child = self.decode(temp)
                new_node.children.append(child)
                temp = temp.right

        return new_node
