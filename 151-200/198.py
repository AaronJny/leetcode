class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0 for _ in nums]
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], dp[i - 1])
            else:
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]