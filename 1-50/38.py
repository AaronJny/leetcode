class Solution:
    dp = []

    def dfs(self, n):
        if self.dp[n]:
            return self.dp[n]
        if n == 1:
            self.dp[n] = "1"
            return self.dp[n]
        else:
            last_str = self.dfs(n - 1)
            slen = len(last_str)
            cnt = 0
            i = 0
            ch = None
            tmps = []
            while i < slen:
                if ch is None:
                    ch = last_str[i]
                if ch == last_str[i]:
                    cnt += 1
                    i += 1
                else:
                    tmps.append(str(cnt))
                    tmps.append(ch)
                    cnt = 0
                    ch = None
            if ch:
                tmps.append(str(cnt))
                tmps.append(ch)
            self.dp[n] = ''.join(tmps)
            return self.dp[n]

    def countAndSay(self, n: int) -> str:
        if len(self.dp) == 0:
            for _ in range(40):
                self.dp.append(None)
        return self.dfs(n)