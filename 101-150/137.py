class Solution:
    def singleNumber(self, nums) -> int:
        m = 0
        n = 0
        for num in nums:
            m = m ^ num & (~n)
            n = n ^ num & (~m)
        return m | n