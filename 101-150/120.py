class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        if n == 1:
            return triangle[0][0]
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]
        for row in range(n - 2, -1, -1):
            for col in range(row+1):
                dp[row][col] = triangle[row][col] + min(dp[row + 1][col], dp[row + 1][col + 1])
        return dp[0][0]