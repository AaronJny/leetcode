# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def dfs(self, index: int, root: TreeNode, show_list: list):
        if index + 1 > len(show_list):
            show_list.append(root.val)
        else:
            show_list[index] = root.val
        if root.left:
            self.dfs(index + 1, root.left, show_list)
        if root.right:
            self.dfs(index + 1, root.right, show_list)

    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        show_list = []
        self.dfs(0, root, show_list)
        return show_list