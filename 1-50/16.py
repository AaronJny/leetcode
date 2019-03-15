class Solution(object):

    def bin_search(self, nums, key, left, right):
        """
        在nums[left:right+1]中查找key，
        当key存在nums中时，返回key的坐标；
        当key不存在时，返回迭代后的left坐标
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
        return left

    def get_close_num(self, nums, pos, need_num, left_limit):
        """
        在nums[left_limit+1:]中，
        比较坐标pos和坐标 pos +1/-1(如果存在)对应的值和need_num的差值，
        找出最接近need_num的数并返回
        :param nums:
        :param pos:
        :param need_num:
        :param left_limit:
        :return:
        """
        # 超出范围
        if pos >= len(nums):
            pos -= 1
        # 默认nums[pos]与need_num最接近
        close_num = nums[pos]
        # 如果pos-1在范围内，比较nums[pos]和nums[pos-1]谁和need_num更接近
        if pos > left_limit + 1:
            if abs(need_num - nums[pos - 1]) < abs(need_num - close_num):
                close_num = nums[pos - 1]
        # 如果nums[pos+1]在范围内，就也比较nums[pos+1]
        if pos < len(nums) - 1:
            if abs(need_num - nums[pos + 1]) < abs(need_num - close_num):
                close_num = nums[pos + 1]
        # 返回最接近need_num的数
        return close_num

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        # 排序，便于二分查找
        nums = sorted(nums)
        close_num = 0
        # 初始赋一个极大值
        close_dist = 1 << 30
        # 枚举前两个数
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                # 计算target-a-b
                tmp_sum_1 = nums[i] + nums[j]
                need_num = target - tmp_sum_1
                # 二分查找target-a-b
                pos = self.bin_search(nums, need_num, j + 1, length - 1)
                # 根据坐标找到使当前abs(target-a-b-c)最小的c
                tmp_close_num = self.get_close_num(nums, pos, need_num, j)
                tmp_sum = tmp_sum_1 + tmp_close_num
                tmp_close_dist = abs(target - tmp_sum)
                # 和全局最接近结果进行比较
                if tmp_close_dist < close_dist:
                    # 更接近则替换
                    close_num = tmp_sum
                    close_dist = tmp_close_dist
                # 当差值为0时，已经是最接近的结果了，就可以提前结束
                if close_dist == 0:
                    return target
        # 返回和target最接近的数
        return close_num
