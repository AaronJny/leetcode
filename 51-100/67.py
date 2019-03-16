class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        n = len(a)
        m = len(b)
        if n == 0:
            return a
        if m == 0:
            return b
        cnt1 = n - 1
        cnt2 = m - 1
        add = 0
        while cnt1 >= 0 and cnt2 >= 0:
            num1 = int(a[cnt1])
            num2 = int(b[cnt2])
            num = num1 + num2 + add
            add = num // 2
            result.append(num % 2)
            cnt1 -= 1
            cnt2 -= 1
        while cnt1 >= 0:
            num = int(a[cnt1]) + add
            add = num // 2
            result.append(num % 2)
            cnt1 -= 1
        while cnt2 >= 0:
            num = int(b[cnt2]) + add
            add = num // 2
            result.append(num % 2)
            cnt2 -= 1
        if add:
            result.append(add)
        return ''.join(map(str, result[::-1]))