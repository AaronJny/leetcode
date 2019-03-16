class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            s = 0
            m = i + 1
            if m < n + 1:
                s += dp[m]
            m = i + 2
            if m < n + 1:
                s += dp[m]
            dp[i] = s
        return dp[0]