class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while True:
            if i * i > x:
                break
            i += 1
        return i - 1