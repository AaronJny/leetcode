from collections import namedtuple

SumNum = namedtuple('SumNum', 'sum,x,y,pos_x,pos_y')


class Solution:
    result = set()

    def bin_search(self, nums, left, right, target):
        """
        二分查找，找到就返回相应坐标，找不到就返回-1
        :param nums:
        :param left:
        :param right:
        :param target:
        :return:
        """
        while left <= right:
            mid = (left + right) >> 1
            x: SumNum = nums[mid]
            if x.sum == target:
                return mid
            elif x.sum > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def find_equal(self, cur_pos, find_pos, sumnums):
        """
        从find_pos向左右两边延伸，处理每一个与sumnums[find_pos].sum值相等的元素
        判断处理到的元素与sumnums[cur_pos]的两个坐标是否有交集，有则放弃，无则加入结果集
        :param cur_pos:
        :param find_pos:
        :param sumnums:
        :return:
        """
        num = sumnums[find_pos].sum
        cur_sumnum = sumnums[cur_pos]
        # 向左延伸，处理所有值和num相等的元素
        left_pos = find_pos
        while left_pos >= 0 and sumnums[left_pos].sum == num:
            tmp_sumnum = sumnums[left_pos]
            # 判断坐标是否有重复，因为原始列表中的每个数字只能使用一次，所以如果有重复就不是正确答案
            if cur_sumnum.pos_x != tmp_sumnum.pos_x and cur_sumnum.pos_x != tmp_sumnum.pos_y and cur_sumnum.pos_y != tmp_sumnum.pos_x and cur_sumnum.pos_y != tmp_sumnum.pos_y:
                # 如果没有重复，将排序后的四元组加入到结果集中（这么做是为了避免不同字典序产生的重复问题）
                self.result.add(tuple(sorted([cur_sumnum.x, cur_sumnum.y, tmp_sumnum.x, tmp_sumnum.y])))
            left_pos -= 1
        # 向右延伸，处理方法同上
        right_pos = find_pos + 1
        while right_pos < len(sumnums) and sumnums[right_pos].sum == num:
            tmp_sumnum = sumnums[right_pos]
            if cur_sumnum.pos_x != tmp_sumnum.pos_x and cur_sumnum.pos_x != tmp_sumnum.pos_y and cur_sumnum.pos_y != tmp_sumnum.pos_x and cur_sumnum.pos_y != tmp_sumnum.pos_y:
                self.result.add(tuple(sorted([cur_sumnum.x, cur_sumnum.y, tmp_sumnum.x, tmp_sumnum.y])))
            right_pos += 1

    def fourSum(self, nums, target: int):
        # 清空结果集
        self.result.clear()
        # 排序
        nums = sorted(nums)
        # 计算两两之和，作为新的列表
        sumnums = [SumNum(nums[i] + nums[j], nums[i], nums[j], i, j) for i in range(len(nums)) for j in
                   range(i + 1, len(nums))]
        # 排序
        sumnums = sorted(sumnums)
        # 枚举新列表中的每个元素
        for i in range(len(sumnums)):
            # 在新列表中查找target-sumnums[i].sum
            pos = self.bin_search(sumnums, i + 1, len(sumnums) - 1, target - sumnums[i].sum)
            # 如果找到了
            if pos != -1:
                # 就进一步进行处理，并加入到结果集中
                self.find_equal(i, pos, sumnums)
        return list(self.result)
