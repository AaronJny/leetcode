class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        lmin = [0 for _ in range(n)]
        for i in range(n):
            if i == 0:
                lmin[i] = prices[i]
            else:
                lmin[i] = min(prices[i], lmin[i - 1])
        rmax = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                rmax[i] = prices[i]
            else:
                rmax[i] = max(prices[i], rmax[i + 1])
        result = 0
        for i in range(n):
            result = max(result, rmax[i] - lmin[i])
        return result