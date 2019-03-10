class Solution:
    def lower_bin_search(self, nums, left, right, target):
        while left < right:
            mid = (left + right) >> 1
            print(mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] >= target:
            return left
        else:
            return left + 1

    def searchInsert(self, nums, target: int) -> int:
        if len(nums) == 0:
            return 0
        return self.lower_bin_search(nums, 0, len(nums) - 1, target)