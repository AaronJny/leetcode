class Solution:

    def simple_multiply(self, num1, num2, zero_num):
        cnt1 = len(num1) - 1
        add = 0
        tmps = [0 for _ in range(zero_num)]
        num = int(num2)
        while cnt1 >= 0:
            x = int(num1[cnt1])
            z = x * num + add
            add = int(z / 10)
            tmps.append(z % 10)
            cnt1 -= 1
        if add != 0:
            tmps.append(add)
        return tmps[::-1]

    def simple_add(self, num1, num2):
        cnt1 = len(num1) - 1
        cnt2 = len(num2) - 1
        add = 0
        tmps = []
        while cnt2 >= 0 and cnt1 >= 0:
            x = num1[cnt1] + num2[cnt2] + add
            add = int(x / 10)
            tmps.append(x % 10)
            cnt2 -= 1
            cnt1 -= 1
        while cnt2 >= 0:
            x = num2[cnt2] + add
            add = int(x / 10)
            tmps.append(x % 10)
            cnt2 -= 1
        while cnt1 >= 0:
            x = num1[cnt1] + add
            add = int(x / 10)
            tmps.append(x % 10)
            cnt1 -= 1
        if add != 0:
            tmps.append(add)
        return tmps[::-1]

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n1 = len(num1)
        n2 = len(num2)
        if n1 >= n2:
            num11 = num1
            num22 = num2
        else:
            num11 = num2
            num22 = num1
        n2 = len(num22)
        adds = []
        for i in range(n2 - 1, -1, -1):
            adds.append(self.simple_multiply(num11, num22[i], n2 - 1 - i))
        sum = [0, ]
        for num in adds:
            sum = self.simple_add(sum, num)
        return ''.join(map(str, sum))