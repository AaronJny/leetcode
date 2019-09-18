class Solution:

    def countPrimes(self, n: int) -> int:
        is_primes = [True for _ in range(n)]
        for i in range(min(n, 2)):
            is_primes[i] = False
        cnt = 0
        for i in range(2, n):
            if is_primes[i]:
                cnt += 1
                for j in range(i + i, n, i):
                    is_primes[j] = False
        return cnt