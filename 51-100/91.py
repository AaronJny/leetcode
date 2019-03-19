class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        if s[0] == '0':
            return 0
        dp[0] = 1
        for i in range(1, n):
            if s[i] == '0' and s[i - 1] != '1' and s[i - 1] != '2':
                dp[i] = 0
                continue
            if s[i - 1] == '0' and dp[i - 1] == 0:
                dp[i] = 0
                continue
            if s[i] == '0':
                tmp = 0
            else:
                tmp = dp[i - 1]
            x = int(s[i - 1:i + 1])
            if 10 <= x <= 26:
                if i - 2 >= 0:
                    tmp += dp[i - 2]
                else:
                    tmp += 1
            dp[i] = tmp
        return dp[n - 1]