class Solution:
    dp = None

    def dfs(self, n, m, row, col):
        if self.dp[row][col] != -1:
            return self.dp[row][col]
        if row == n and col == m:
            self.dp[row][col] = 1
            return self.dp[row][col]
        result = 0
        ncol = col + 1
        if ncol <= m:
            result += self.dfs(n, m, row, ncol)
        nrow = row + 1
        if nrow <= n:
            result += self.dfs(n, m, nrow, col)
        self.dp[row][col] = result
        return self.dp[row][col]

    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = [[-1 for i in range(m + 10)] for j in range(n + 10)]
        return self.dfs(n, m, 1, 1)