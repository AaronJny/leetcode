class Solution:

    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        left = 0
        right = n - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 1:
                if nums[left] != 1:
                    left = i
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1