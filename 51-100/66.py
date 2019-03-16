class Solution:
    def plusOne(self, digits):
        add = 1
        n = len(digits)
        result = []
        for i in range(n - 1, -1, -1):
            num = digits[i] + add
            add = num // 10
            result.append(num % 10)
        if add:
            result.append(add)
        return result[::-1]