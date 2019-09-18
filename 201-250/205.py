class Solution:

    def format_str(self, s):
        """
        将给定字符串转成数字编码的列表

        Args:
            s:

        Returns:

        """
        ch_num_map = {}
        current_num = 1
        format_seqs = []
        for ch in s:
            num = ch_num_map.get(ch, 0)
            # 没有对应的数字编号，就生成一个
            if not num:
                ch_num_map[ch] = current_num
                num = current_num
                current_num += 1
            format_seqs.append(num)
        del ch_num_map
        return format_seqs

    def isIsomorphic(self, s: str, t: str) -> bool:
        seqs1 = self.format_str(s)
        seqs2 = self.format_str(t)
        return seqs1 == seqs2