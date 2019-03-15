class Solution:

    def dfs(self, pos, n, nums, used, second_nums, result):
        if pos == n:
            result.append(tuple(second_nums))
            return
        for i in range(n):
            if used[i]:
                used[i] = False
                second_nums[pos] = nums[i]
                self.dfs(pos + 1, n, nums, used, second_nums, result)
                used[i] = True

    def permute(self, nums):
        result = []
        n = len(nums)
        used = [True for _ in range(n)]
        second_nums = [0 for _ in range(n)]
        self.dfs(0, n, nums, used, second_nums, result)
        return list(set(result))