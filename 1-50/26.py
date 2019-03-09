class Solution:
    def removeDuplicates(self, nums) -> int:
        nums_len = len(nums)
        i = 0
        while i < nums_len - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
                nums_len -= 1
            else:
                i += 1
        return len(nums)