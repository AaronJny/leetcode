# coding=utf-8

class Solution:

    def bin_search(self, nums, key, left, right):
        while left <= right:
            mid = (left + right) / 2
            if key == nums[mid]:
                return mid
            elif key < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums = sorted(nums)
        threesums = set()
        for i in range(length - 2):
            if nums[i] > 0:
                break
            for j in range(i + 1, length - 1):
                tmp_sum = nums[i] + nums[j]
                if tmp_sum > 0:
                    break
                pos = self.bin_search(nums, -tmp_sum, j + 1, length - 1)
                if pos != -1:
                    threesums.add((nums[i], nums[j], nums[pos]))
        return list(threesums)


