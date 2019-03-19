class Solution:
    def dfs(self, pos, n, subsets: set, tmps: list, nums):
        if pos == n:
            subsets.add(tuple(tmps))
        else:
            # 选择
            tmps.append(nums[pos])
            self.dfs(pos + 1, n, subsets, tmps, nums)
            tmps.pop()
            # 不选择
            self.dfs(pos + 1, n, subsets, tmps, nums)

    def subsets(self, nums):
        n = len(nums)
        subsets = set()
        tmps = []
        self.dfs(0, n, subsets, tmps, nums)
        return [list(x) for x in list(subsets)]