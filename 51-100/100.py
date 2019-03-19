# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, p: TreeNode, q: TreeNode):
        # print(p.val, p.left, p.right, q.val, q.left, q.right)
        # 如果两个是叶子节点
        if not (p.left or p.right or q.left or q.right):
            # 值相等就相同
            if p.val == q.val:
                return True
            # 否则不相同
            else:
                return False
        # 不是叶子节点
        else:
            # 比较当前值
            if p.val != q.val:
                return False
            # 都有左节点，则比较左节点
            if p.left and q.left:
                flag = self.dfs(p.left, q.left)
            # 其中一个有左节点，另一个没有，则不相同
            elif p.left or q.left:
                return False
            # 都没有左节点，认为左边相同
            else:
                flag = True
            # 已经判断出不相同时，就直接返回
            if not flag:
                return False
            # 否则，还要看右节点

            # 都有右节点，则比较右节点
            if p.right and q.right:
                return self.dfs(p.right, q.right)
            # 其中一个有，则不相同
            elif p.right or q.right:
                return False
            # 否则，认为都相同
            else:
                return True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return self.dfs(p, q)
        elif p or q:
            return False
        else:
            return True