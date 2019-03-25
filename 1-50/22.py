class Solution:
    # 最终的结果集
    result = set()
    # 用于临时存储递归生成的一种合法组合的列表
    curstring = []

    def dfs(self, leftcnt, rightcnt):
        """
        递归搜索所有可能的合法组合，并加入到结果集中
        :param leftcnt: 剩余可用左括号数
        :param rightcnt: 剩余可用右括号数
        :return:
        """
        # 当左右括号都用完了时，就得到了一个合法结果
        if leftcnt == 0 and rightcnt == 0:
            # 将组合拼接成字符串，加入结果集中
            self.result.add(''.join(self.curstring))
        # 现在，有两种放置方法，分别是在这里放左括号和右括号
        # 先看左括号，当左括号还有剩余时，就可以放置
        if leftcnt > 0:
            # 放置左括号
            self.curstring.append('(')
            # 剩余可用左括号的数量-1，继续放置下一个
            self.dfs(leftcnt - 1, rightcnt)
            # 回溯，撤销放置，尝试其他放置方法
            self.curstring.pop()
        # 再看右括号，当右括号还有剩余时
        if rightcnt > 0:
            # 并不能直接放置，还要满足剩余右括号的数量大于剩余左括号的数量才行
            # 也就是我们之前说的
            # `假设s是一个合法的括号组合，则在s的任意位置，左边的左括号的数量一定大于等于右括号的数量`
            if rightcnt - leftcnt > 0:
                # 放置右括号
                self.curstring.append(')')
                # 剩余可用右括号数量-1，继续放置下一个
                self.dfs(leftcnt, rightcnt - 1)
                # 回溯，撤销放置
                self.curstring.pop()

    def generateParenthesis(self, n: int):
        # 清空结果集
        self.result.clear()
        # 清空临时列表
        self.curstring.clear()
        # 递归搜索所有符合条件的结果
        self.dfs(n, n)
        # 结果获取完毕，以列表的形式返回结果
        return list(self.result)
