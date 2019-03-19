from collections import Counter


class Solution:
    def check_counter(self, s_counter, t_counter):
        for key, value in t_counter.items():
            x = s_counter.get(key, 0)
            if x < value:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if n == 0 or m == 0 or m > n:
            return ''
        t_counter = Counter(t)
        s_counter = Counter()
        left = 0
        right = 0
        result_left = 0
        result_right = 0
        INF = 1 << 30
        min_length = INF
        while right < n:
            if s[right] in t_counter:
                s_counter[s[right]] += 1
                while left <= right and self.check_counter(s_counter, t_counter):
                    tmp = right - left + 1
                    if tmp < min_length:
                        min_length = tmp
                        result_left = left
                        result_right = right
                    s_counter[s[left]] -= 1
                    if s_counter[s[left]] <= 0:
                        s_counter.pop(s[left])
                    left += 1
            right += 1
        if min_length == INF:
            return ''
        else:
            return s[result_left:result_right + 1]
