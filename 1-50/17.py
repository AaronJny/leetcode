class Solution:
    # 存放所有可能的字符串的列表
    combinations = []

    # 数字到字母的映射关系
    digits_chr_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    # 临时存放一种可能字符串的列表
    # 每次深搜+回溯的时候都会修改它
    tmp_chrs = []

    def dfs(self, digits, pos, n):
        """
        当pos<n时，将数字digits[pos]转换成一个符合条件的字母
        :param digits:数字串
        :param pos: 当前处理坐标
        :param n: 数字串的长度
        :return:
        """
        # 当所有数字都被处理完成时
        if pos >= n:
            # 将临时列表中的字母拼接成字符串，保存到结果列表中取
            self.combinations.append(''.join(self.tmp_chrs))
        # 否则
        else:
            num = digits[pos]
            # 获取当前数字对应的字母列表
            chrs = self.digits_chr_map.get(num)
            # 对于每一个可以使用的字母
            for chr in chrs:
                # 尝试选用它
                self.tmp_chrs.append(chr)
                # 然后递归去选择下一个字母
                self.dfs(digits, pos + 1, n)
                # 回溯，撤销选择，以尝试其他选择
                self.tmp_chrs.pop()

    def letterCombinations(self, digits: str):
        # 清空结果集
        self.combinations.clear()
        # 清空临时列表
        self.tmp_chrs.clear()
        # 数字串为空的时候，直接返回空列表
        if len(digits) == 0:
            return []
        # 否则，就计算这个数字串对应的所有可能字符串，并加入到结果集中
        self.dfs(digits, 0, len(digits))
        # 返回结果集的列表形式
        return list(self.combinations)
