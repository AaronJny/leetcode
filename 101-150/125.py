import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmps = []
        words = set([ch for ch in string.ascii_lowercase] + [str(num) for num in range(10)])
        for ch in s.lower():
            if ch in words:
                tmps.append(ch)
        x = ''.join(tmps)
        return x == x[::-1]