class Solution:
    combination = []

    result = set()

    def dfs(self, candidates, target, curpos, cursum, n):
        if curpos >= n:
            return
        if cursum > target:
            return
        if cursum == target:
            self.result.add(tuple(self.combination))
            return
        num = candidates[curpos]
        next_sum = cursum + num
        # 使用当前数字，且下次仍然使用这个数字
        self.combination.append(candidates[curpos])
        self.dfs(candidates, target, curpos, next_sum, n)
        # 使用当前数字，且下次尝试使用下一个数字
        self.dfs(candidates, target, curpos + 1, next_sum, n)
        self.combination.pop()
        # 不使用当前数字，且下次尝试使用下一个数字
        self.dfs(candidates, target, curpos + 1, cursum, n)

    def combinationSum(self, candidates, target: int):
        self.result.clear()
        self.combination.clear()
        self.dfs(candidates, target, 0, 0, len(candidates))
        return list(self.result)