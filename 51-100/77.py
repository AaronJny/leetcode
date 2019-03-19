class Solution:
    def dfs(self, pos, m, n, k, tmps, combines):
        if pos == k:
            combines.append(tmps.copy())
        else:
            for i in range(m + 1, n + 1):
                tmps.append(i)
                self.dfs(pos + 1, i, n, k, tmps, combines)
                tmps.pop()

    def combine(self, n: int, k: int):
        tmps = []
        combines = []
        self.dfs(0, 0, n, k, tmps, combines)
        return combines