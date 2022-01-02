from typing import Optional

from Tree import TreeNode


# https://leetcode.com/problems/serialize-and-deserialize-bst
# As its BST, just serialize the postorder or preorder string.
# Then use inorder + (post/pre)order to build the tree

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        As we are implementing for BST, no need to serialize the inorder version as its just a sorted postorder
        """
        return ' '.join(map(str, self.postorder(root)))

    def postorder(self, root):
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        postorder_list = list(map(int, data.split(' ')))
        inorder_list = sorted(postorder_list)
        tree = self.buildTree(inorder_list, postorder_list)
        return tree

    def buildTree(self, inorder_list, postorder_list):
        postorder_index = len(postorder_list) - 1

        inorder_pos = {x: i for i, x in enumerate(inorder_list)}

        def buildTreeInner(l, r):
            nonlocal postorder_index
            if l > r:
                return None

            index = inorder_pos[postorder_list[postorder_index]]
            node = TreeNode(postorder_list[postorder_index])
            postorder_index -= 1

            node.right = buildTreeInner(index + 1, r)
            node.left = buildTreeInner(l, index - 1)
            return node

        return buildTreeInner(0, postorder_index)
