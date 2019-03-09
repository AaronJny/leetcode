class Solution:
    result = set()
    curstring = []

    def dfs(self, leftcnt, rightcnt):
        if leftcnt == 0 and rightcnt == 0:
            self.result.add(''.join(self.curstring))
        if leftcnt > 0:
            self.curstring.append('(')
            self.dfs(leftcnt - 1, rightcnt)
            self.curstring.pop()
        if rightcnt > 0:
            if rightcnt - leftcnt > 0:
                self.curstring.append(')')
                self.dfs(leftcnt, rightcnt - 1)
                self.curstring.pop()

    def generateParenthesis(self, n: int):
        self.result.clear()
        self.curstring.clear()
        self.dfs(n, n)
        return list(self.result)