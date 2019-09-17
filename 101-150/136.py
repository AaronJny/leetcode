class Solution:
    def singleNumber(self, nums) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x