from collections import namedtuple

SumNum = namedtuple('SumNum', 'sum,x,y,pos_x,pos_y')


class Solution:
    result = set()

    def bin_search(self, nums, left, right, target):
        while left < right:
            mid = int((left + right) / 2)
            x: SumNum = nums[mid]
            if x.sum == target:
                return mid
            elif x.sum > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def find_equal(self, cur_pos, find_pos, sumnums):
        num = sumnums[find_pos].sum
        cur_sumnum = sumnums[cur_pos]
        left_pos = find_pos
        while left_pos >= 0 and sumnums[left_pos].sum == num:
            tmp_sumnum = sumnums[left_pos]
            if cur_sumnum.pos_x != tmp_sumnum.pos_x and cur_sumnum.pos_x != tmp_sumnum.pos_y and cur_sumnum.pos_y != tmp_sumnum.pos_x and cur_sumnum.pos_y != tmp_sumnum.pos_y:
                self.result.add(tuple(sorted([cur_sumnum.x, cur_sumnum.y, tmp_sumnum.x, tmp_sumnum.y])))
            left_pos -= 1
        right_pos = find_pos + 1
        while right_pos < len(sumnums) and sumnums[right_pos].sum == num:
            tmp_sumnum = sumnums[right_pos]
            if cur_sumnum.pos_x != tmp_sumnum.pos_x and cur_sumnum.pos_x != tmp_sumnum.pos_y and cur_sumnum.pos_y != tmp_sumnum.pos_x and cur_sumnum.pos_y != tmp_sumnum.pos_y:
                self.result.add(tuple(sorted([cur_sumnum.x, cur_sumnum.y, tmp_sumnum.x, tmp_sumnum.y])))
            right_pos += 1

    def fourSum(self, nums, target: int):
        self.result.clear()
        nums = sorted(nums)
        sumnums = [SumNum(nums[i] + nums[j], nums[i], nums[j], i, j) for i in range(len(nums)) for j in
                   range(i + 1, len(nums))]
        sumnums = sorted(sumnums)
        for i in range(len(sumnums)):
            pos = self.bin_search(sumnums, i + 1, len(sumnums) - 1, target - sumnums[i].sum)
            if pos != -1:
                self.find_equal(i, pos, sumnums)
        return list(self.result)