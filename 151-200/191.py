class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        cnt = 0
        while n:
            if n & 1:
                cnt += 1
            n = n >> 1
        return cnt