class Solution(object):

    def bin_search(self, nums, key, left, right):
        while left <= right:
            mid = (left + right) / 2
            if key == nums[mid]:
                return mid
            elif key < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def get_close_num(self, nums, pos, need_num, left_limit):
        if pos >= len(nums):
            pos -= 1
        close_num = nums[pos]
        if pos > left_limit + 1:
            if abs(need_num - nums[pos - 1]) < abs(need_num - close_num):
                close_num = nums[pos - 1]
        if pos < len(nums) - 1:
            if abs(need_num - nums[pos + 1]) < abs(need_num - close_num):
                close_num = nums[pos + 1]
        return close_num

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        nums = sorted(nums)
        close_num = 0
        close_dist = 1 << 30
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                tmp_sum_1 = nums[i] + nums[j]
                need_num = target - tmp_sum_1
                pos = self.bin_search(nums, need_num, j + 1, length - 1)
                tmp_close_num = self.get_close_num(nums, pos, need_num, j)
                tmp_sum = tmp_sum_1 + tmp_close_num
                tmp_close_dist = abs(target - tmp_sum)
                if tmp_close_dist < close_dist:
                    close_num = tmp_sum
                    close_dist = tmp_close_dist
                if close_dist == 0:
                    return target
        return close_num