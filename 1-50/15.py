# coding=utf-8

class Solution:

    def bin_search(self, nums, key, left, right):
        """
        二分查找key是否在nums里面，
        存在则返回任何一个值等于key的数组下标，
        不存在则返回-1
        :param nums:
        :param key:
        :param left:
        :param right:
        :return:
        """
        while left <= right:
            mid = (left + right) >> 1
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
        # 先排序，后面才能用二分查找
        nums = sorted(nums)
        # 所有符合条件的组合的结果集
        threesums = set()
        # 枚举前两个数
        for i in range(length - 2):
            if nums[i] > 0:
                break
            for j in range(i + 1, length - 1):
                tmp_sum = nums[i] + nums[j]
                if tmp_sum > 0:
                    break
                # 在数组中二分查找（0-tmp_sum）
                pos = self.bin_search(nums, -tmp_sum, j + 1, length - 1)
                if pos != -1:
                    # 找到了，就保存结果
                    threesums.add((nums[i], nums[j], nums[pos]))
        # 根据题目要求，以list的形式返回数据
        return list(threesums)
