from Tree import TreeNode


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# Medium
# T = O(N)
# S = O(N)

def lowestCommonAncestor_myVersion(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def compute_path_to(node, search, path):
        if not node:
            return []

        if node == search:
            return path + [node]

        res = compute_path_to(node.left, search, path + [node])

        return res or compute_path_to(node.right, search, path + [node])

    p_path = compute_path_to(root, p, [root])
    q_path = compute_path_to(root, q, [root])

    i = 0
    length = min(len(p_path), len(q_path))
    while i < length and p_path[i] == q_path[i]:
        i += 1

    return p_path[i - 1]


# got rid of the path check
# here we are only looking for count of matches from left, right and mid

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    ans = None

    def lca(node):
        nonlocal ans
        if not node:
            return False

        left = lca(node.left)
        right = lca(node.right)

        mid = node == p or node == q

        if left + mid + right >= 2:
            ans = node

        return mid or left or right

    lca(root)
    return ans
