class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        i = 0
        n = len(nums)
        # 移除掉非负数字
        while i < n:
            if nums[i] < 1:
                nums.pop(i)
                n -= 1
            else:
                i += 1
        # 将小于n的数通过负号标记，映射到数组上
        for i in range(n):
            pos = abs(nums[i]) - 1
            if pos < n:
                nums[pos] = -abs(nums[pos])
        # 没有被标记的坐标+1就是缺的数
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        # 全部都被标记了，说明数组的数字刚好为1～n,那么最小的是n+1
        return n + 1
