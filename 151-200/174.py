class Solution:

    def calculateMinimumHP(self, dungeon) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[0 for col in range(m)] for row in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # 最右下角
                if i == n - 1 and j == m - 1:
                    if dungeon[i][j] >= 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(1, 1 - dungeon[i][j])
                # 最后一行或一列，需要特殊处理
                elif i == n - 1 or j == m - 1:
                    if i == n - 1:
                        n_least = dp[i][j + 1]
                    else:
                        n_least = dp[i + 1][j]
                    least = max(1, n_least - dungeon[i][j])
                    dp[i][j] = least
                # 其他的，直接比较右边的和下边的临近格子
                else:
                    dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        # s = '\n'.join(' '.join('{}'.format(x) for x in row) for row in dungeon)
        # print(s)
        # print('*' * 40)
        # s = '\n'.join(' '.join('{}'.format(x) for x in row) for row in dp)
        # print(s)
        return max(1, dp[0][0])
