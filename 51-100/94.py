# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root: TreeNode, result: list):
        if root.left:
            self.dfs(root.left, result)
        result.append(root.val)
        if root.right:
            self.dfs(root.right, result)

    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        result = []
        self.dfs(root, result)
        return result