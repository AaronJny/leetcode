class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        i = 0
        while i + needle_len <= haystack_len:
            if haystack[i:i + needle_len] == needle:
                return i
            i += 1
        return -1