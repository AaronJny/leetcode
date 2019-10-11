class Solution:
    def minSubArrayLen(self, s: int, nums: list) -> int:
        min_len = 0
        if not nums:
            return 0
        length = len(nums)
        l = 0
        _sum = 0
        for i in range(length):
            # 如果小于，就加进去
            r = i + 1
            _sum += nums[i]
            for j in range(l, r):
                if _sum - nums[j] >= s:
                    l += 1
                    _sum -= nums[j]
                else:
                    break
            if _sum >= s and (min_len == 0 or min_len > r - l):
                min_len = r - l
        return min_len