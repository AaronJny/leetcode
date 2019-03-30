class Solution:
    def dfs(self, s, left, right, n, tmp, result):
        # 全部处理完了，加入到结果中
        if left >= n:
            result.add(tuple(tmp))
        else:
            # 尝试在这里切割
            x = s[left:right + 1]
            if x == x[::-1]:
                tmp.append(x)
                self.dfs(s, right + 1, right + 1, n, tmp, result)
                tmp.pop()
            # 尝试不切割
            if right + 1 < n:
                self.dfs(s, left, right + 1, n, tmp, result)

    def partition(self, s: str):
        n = len(s)
        if n == 0:
            return []
        if n == 1:
            return [[s, ], ]
        tmp = []
        result = set()
        self.dfs(s, 0, 0, n, tmp, result)
        return [list(item) for item in result]