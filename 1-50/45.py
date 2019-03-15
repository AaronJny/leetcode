class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        cur_pos = 0
        step = 0
        while cur_pos <= n:
            if cur_pos == n - 1:
                return step
            if cur_pos + nums[cur_pos] >= n - 1:
                return step + 1
            max_pos = cur_pos + 1
            for i in range(cur_pos + 1, min(nums[cur_pos] + cur_pos + 1, n)):
                if nums[i] + i > nums[max_pos] + max_pos:
                    max_pos = i
            cur_pos = max_pos
            step += 1
        return step