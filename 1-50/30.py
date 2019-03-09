from collections import Counter


class Solution:

    def findSubstring(self, s: str, words):
        if s == "" or len(words) == 0:
            return []
        n = len(s)
        wordlen = len(words[0])
        wordnum = len(words)
        words_counter = Counter(words)
        need_length = wordnum * wordlen
        result = []
        for i in range(n - need_length + 1):
            tmp_counter = words_counter.copy()
            for j in range(i, i + need_length, wordlen):
                tmp_counter[s[j:j + wordlen]] -= 1
            for key, value in tmp_counter.items():
                if value > 0:
                    flag = False
                    break
            else:
                flag = True
            del tmp_counter
            if flag:
                result.append(i)
        return result