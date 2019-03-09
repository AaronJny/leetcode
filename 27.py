class Solution:
    def removeElement(self, nums, val: int) -> int:
        nums_len = len(nums)
        i = 0
        while i < nums_len:
            if nums[i] == val:
                nums.pop(i)
                nums_len -= 1
            else:
                i += 1
        return len(nums)
