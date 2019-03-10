class Solution:
    def lower_bin_search(self, nums, left, right, target):
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left > 0 and nums[left - 1] == target:
            return True, left - 1
        if nums[left] == target:
            return True, left
        if left < len(nums) - 1 and nums[left + 1] == target:
            return True, left + 1
        return False, left

    def upper_bin_search(self, nums, left, right, target):
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if right < len(nums) - 1 and nums[right + 1] == target:
            return True, right + 1
        if nums[right] == target:
            return True, right
        if right > 0 and nums[right - 1] == target:
            return True, right - 1

        return False, right

    def searchRange(self, nums, target: int):
        if len(nums) == 0:
            return [-1, -1]
        ok, pos1 = self.lower_bin_search(nums, 0, len(nums) - 1, target)
        if not ok:
            return [-1, -1]
        else:
            ok, pos2 = self.upper_bin_search(nums, 0, len(nums) - 1, target)
            return [pos1, pos2]