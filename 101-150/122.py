class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n < 2:
            return 0
        result = 0
        current_price = -1
        i = 0
        while i < n:
            # 当等待购入时，找到单调递减时的最低点
            if current_price == -1:
                while i + 1 < n and prices[i] >= prices[i + 1]:
                    i += 1
                current_price = prices[i]
                i += 1
            # 当等待卖出时，找到单调递增时的最高点
            else:
                # 单调递增
                while i + 1 < n and prices[i] <= prices[i + 1]:
                    i += 1
                # 最高点都比现在价格低，就忽略
                if prices[i] <= current_price:
                    i += 1
                    continue
                # 否则，卖出
                result += prices[i] - current_price
                current_price = -1
                i += 1
        return result