class Solution:
    def bin_check(self, nums):
        length = len(nums)
        l = 0
        r = length-1
        while l < r:
            mid = (l + r) >> 1
            # 当已达到左边边界时
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    l = mid + 1
            # 当达到右边边界时
            elif mid == length:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    r = mid - 1
            # 在中间时
            else:
                if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid - 1] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return l

    def findPeakElement(self, nums) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        return self.bin_check(nums)