class Solution:
    combination = []

    result = set()

    def dfs(self, candidates, target, curpos, cursum, n):
        if curpos >= n:
            if cursum == target:
                self.result.add(tuple(sorted(self.combination)))
            return
        if cursum > target:
            return
        if cursum == target:
            self.result.add(tuple(sorted(self.combination)))
            return
        num = candidates[curpos]
        next_sum = cursum + num
        # 使用当前数字，且下次尝试使用下一个数字
        self.combination.append(candidates[curpos])
        self.dfs(candidates, target, curpos + 1, next_sum, n)
        self.combination.pop()
        # 不使用当前数字，且下次尝试使用下一个数字
        self.dfs(candidates, target, curpos + 1, cursum, n)

    def combinationSum2(self, candidates, target: int):
        self.result.clear()
        self.combination.clear()
        self.dfs(candidates, target, 0, 0, len(candidates))
        return list(self.result)