class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums) - 1
        if nums[0] >= n:
            return True
        pos = 0
        while pos <= n:
            if pos >= n:
                return True
            npos = nums[pos] + pos
            if npos >= n:
                return True
            max_pos = npos
            for tmp_pos in range(pos + 1, npos):
                if tmp_pos + nums[tmp_pos] > max_pos + nums[max_pos]:
                    max_pos = tmp_pos
            if pos >= max_pos:
                return False
            pos = max_pos
        return True