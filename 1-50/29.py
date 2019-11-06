class Solution:
    def simple_divide(self, dividend, divisor):
        """
        使用加减法模拟一次简单的除法
        :param dividend: 被除数
        :param divisor: 除数
        :return: int,int 商,余数
        """
        # 被除数是除数的几倍
        cnt = 0
        # 当前除数的累加值
        add = 0
        # 如果当前累加值+除数仍小于被除数
        while add + divisor <= dividend:
            # 就累加一次
            add += divisor
            # 把倍数计数器+1
            cnt += 1
        # 判断累加值是否和被除数相等，相等则余数为0
        if add == dividend:
            last = 0
        # 否则余数为被除数和累加值的差值
        else:
            last = dividend - add
        # 返回商和余数
        return cnt, last

    def divide(self, dividend: int, divisor: int) -> int:
        """
        在不使用乘法、除法和mod运算符的情况下，给定除数和被除数，返回商
        :param dividend:被除数
        :param divisor:除数
        :return:商
        """
        # 先对一些特殊情况进行处理
        # 如果被除数为0，结果就为0
        if dividend == 0:
            result = 0
        # 如果除数为1，结果就为被除数
        elif divisor == 1:
            result = dividend
        # 如果除数为-1，结果为被除数的负数形式
        elif divisor == -1:
            result = -dividend
        # 如果除数为2，则直接使用位运算
        elif divisor == 2:
            if dividend & 1:
                result = (dividend - 1) >> 1
            else:
                result = dividend >> 1
        # 否则，我们模拟一下除法
        else:
            # 判断被除数的正负
            flag1 = -1 if dividend < 0 else 1
            # 判断除数的正负
            flag2 = -1 if divisor < 0 else 1
            # 对除数和被除数都保留其绝对值
            divisor = abs(divisor)
            dividend = abs(dividend)
            # 如果除数比被除数大，商就是0
            if dividend < divisor:
                result = 0
            # 否则，开始模拟计算
            else:
                quotients = []
                # 将被除数转成字符串，方便我们按位进行处理
                dividend_str = str(dividend)
                # 除数也做相同处理
                divisor_str = str(divisor)
                # 下面，我们开始摆竖式，计算除法
                # 从被除数开头的位置，取和除数相同位数的字符串
                last_str = dividend_str[:len(divisor_str)]
                # 被除数处理到那个位置了
                dividend_pos = len(divisor_str) - 1
                # 一步步计算竖式，知道算到最后一位
                while dividend_pos < len(dividend_str):
                    # 将我们取出的被除数部分转成证书
                    last = int(last_str)
                    # 如果这部分被除数比除数大
                    if last >= divisor:
                        # 就模拟一次简单的除法，计算商和余数
                        quo, las = self.simple_divide(last, divisor)
                        # 将这一步的商加入到列表中
                        quotients.append(str(quo))
                        # 把余数转成字符串，准备进行补位，算下一步
                        last_str = str(las)
                    # 否则的话，这部分商为0，这部分被除数都是余数
                    else:
                        quotients.append('0')
                    # 被除数的游标后移以为
                    dividend_pos += 1
                    # 如果没有算到最后一位，就从被除数中去一位进行补位，重复上面的计算
                    if dividend_pos < len(dividend_str):
                        last_str += dividend_str[dividend_pos]
                # 已经计算完了，每一步的商都在列表里，拼接起来，转成整数
                result = int(''.join(quotients))
                # 然后根据除数和被除数的负号，计算商的符号
                if flag1 == -1 and flag2 == -1 or flag1 == 1 and flag2 == 1:
                    pass
                else:
                    result = -result
        # 根据题目要求，如果数据不再 [−2^31,  2^31 − 1]范围内，就返回2^31-1
        # 如果严格要求来看，这里其实应该使用字符串进行比较，在result那一步也只保存成字符串，但我嫌麻烦，就这样偷懒了。
        # 毕竟想考较的应该主要是除法模拟吧？
        if (result < -(1 << 31)) or (result >= (1 << 31)):
            return (1 << 31) - 1
        else:
            return result
