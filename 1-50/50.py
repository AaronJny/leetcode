class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return x
        res = 1.0
        flag = 1 if n > 0 else -1
        n = abs(n)
        while n > 0:
            if n & 1:
                res *= x
            x = x * x
            n = n >> 1
        if flag == -1:
            res = 1.0 / res
        return res
