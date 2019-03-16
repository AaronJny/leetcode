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

    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        n = len(obstacleGrid)
        if n == 0:
            return 0
        m = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        self.dp = [[-1 for i in range(m)] for j in range(n)]
        return self.dfs(n - 1, m - 1, 0, 0, obstacleGrid)