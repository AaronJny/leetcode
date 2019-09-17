class Solution:
    def split_num(self, n):
        """
        切分指定的数字，变成一个列表

        Args:
            n:

        Returns:
            list: 个位数组成的列表
        """
        if n < 10:
            return [n, ]
        nums = []
        while n:
            nums.append(n % 10)
            n = n // 10
        return nums

    def calc_square_sum(self, nums):
        """
        计算给定列表中所有数的平方和

        Args:
            nums:

        Returns:

        """
        total = sum([num * num for num in nums])
        return total

    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        cache_set = set()
        while True:
            if n in cache_set:
                return False
            cache_set.add(n)
            nums = self.split_num(n)
            n = self.calc_square_sum(nums)
            if n == 1:
                return True