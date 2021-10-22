from collections import deque
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createBinaryTreeFrom(bin_tree_array: []) -> TreeNode:
    return ___createBinaryTree(bin_tree_array, 0, len(bin_tree_array))


def ___createBinaryTree(bin_tree_array, root_index, length):
    root = None
    if root_index < length:
        root_element = bin_tree_array[root_index]
        if root_element is not None:
            root = TreeNode(bin_tree_array[root_index])
            root.left = ___createBinaryTree(bin_tree_array, 2 * root_index + 1, length)
            root.right = ___createBinaryTree(bin_tree_array, 2 * root_index + 2, length)
    return root


def levelOrder(root: TreeNode) -> []:
    arr = []
    h = height(root)
    for i in range(h):
        arr += getElementsOfLevel(root, i)
    return arr


def toTreeArray(root: TreeNode):
    if root is None:
        return []
    h = height(root)

    arr = [None] * ((2 ** h) - 1)
    arr[0] = root.val

    q = deque()
    q.append((0, root))

    while q:
        index, node = q.popleft()

        if node.left:
            arr[2 * index + 1] = node.left.val
            q.append((2 * index + 1, node.left))
        if node.right:
            arr[2 * index + 2] = node.right.val
            q.append((2 * index + 2, node.right))

    # get rid of trailing Nones

    return arr[:(next(i for i in range(len(arr) - 1, -1, -1) if arr[i] is not None)) + 1]


def getElementsOfLevel(root, level):
    if root is None:
        return []
    if level == 0:
        return [root.val]
    elif level > 0:
        left = getElementsOfLevel(root.left, level - 1)
        right = getElementsOfLevel(root.right, level - 1)
        if not left and not right:
            return []
        if not left and right:
            return [None] + right
        return left + right


def height(root: TreeNode):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1


def invertTree(root: TreeNode) -> TreeNode:
    if root:
        left = root.left
        right = root.right
        root.right = invertTree(left)
        root.left = invertTree(right)
    return root
