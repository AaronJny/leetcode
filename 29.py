class Solution:
    def simple_divide(self, dividend, divisor):
        cnt = 0
        add = 0
        while add + divisor <= dividend:
            add += divisor
            cnt += 1
        if add == dividend:
            last = 0
        else:
            last = dividend - add
        return cnt, last

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            result = 0
        elif divisor == 1:
            result = dividend
        elif divisor == -1:
            result = -dividend
        elif divisor == 2:
            if dividend & 1:
                result = (dividend - 1) >> 1
            else:
                result = dividend >> 1
        else:
            flag1 = -1 if dividend < 0 else 1
            flag2 = -1 if divisor < 0 else 1
            divisor = abs(divisor)
            dividend = abs(dividend)
            if dividend < divisor:
                result = 0
            else:
                quotients = []

                dividend_str = str(dividend)
                divisor_str = str(divisor)
                last_str = dividend_str[:len(divisor_str)]
                dividend_pos = len(divisor_str) - 1
                while dividend_pos < len(dividend_str):
                    last = int(last_str)
                    if last >= divisor:
                        quo, las = self.simple_divide(last, divisor)
                        quotients.append(str(quo))
                        last_str = str(las)
                    else:
                        quotients.append('0')
                    dividend_pos += 1
                    if dividend_pos < len(dividend_str):
                        last_str += dividend_str[dividend_pos]
                result = int(''.join(quotients))
                if flag1 == -1 and flag2 == -1 or flag1 == 1 and flag2 == 1:
                    pass
                else:
                    result = -result
        if (result < -(1 << 31)) or (result >= (1 << 31)):
            return (1 << 31) - 1
        else:
            return result
