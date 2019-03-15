class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0
        max_sum = nums[0]
        xsum = 0
        for num in nums:
            xsum += num
            if max_sum < xsum:
                max_sum = xsum
            if xsum < 0:
                xsum = 0
        return max_sum