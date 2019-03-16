class Solution:
    dp = None

    def dfs(self, n, m, row, col, obstacleGrid):
        if self.dp[row][col] != -1:
            return self.dp[row][col]
        if row == n and col == m:
            self.dp[row][col] = 1
            return self.dp[row][col]
        result = 0
        ncol = col + 1
        if ncol <= m and obstacleGrid[row][ncol] == 0:
            result += self.dfs(n, m, row, ncol, obstacleGrid)
        nrow = row + 1
        if nrow <= n and obstacleGrid[nrow][col] == 0:
            result += self.dfs(n, m, nrow, col, obstacleGrid)
        self.dp[row][col] = result
        return self.dp[row][col]

    def minPathSum(self, grid) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        INF = 1 << 30
        dp = [[0 for i in range(m)] for j in range(n)]
        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if row == n - 1 and col == m - 1:
                    dp[row][col] = grid[row][col]
                else:
                    result = INF
                    nrow = row + 1
                    if nrow < n:
                        result = min(result, dp[nrow][col])
                    ncol = col + 1
                    if ncol < m:
                        result = min(result, dp[row][ncol])
                    dp[row][col] = result + grid[row][col]
        return dp[0][0]