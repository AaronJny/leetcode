class Solution:
    def format_data(self, words, charlen, maxWidth, is_last):
        if is_last:
            res = ' '.join(words)
            res += ' ' * (maxWidth - len(res))
            return res
        else:
            n = len(words)
            if n == 1:
                return words[0] + (' ' * (maxWidth - charlen))
            space_num = maxWidth - charlen
            avg_space_num = space_num // (n - 1)
            left_add = space_num - (avg_space_num * (n - 1))
            space_list = [avg_space_num for _ in range(n)]
            space_list[n - 1] = 0
            for i in range(left_add):
                space_list[i] += 1
            result = []
            for i in range(n):
                result.append(words[i])
                space = ' ' * space_list[i]
                if space:
                    result.append(space)
            return ''.join(result)

    def fullJustify(self, words, maxWidth):
        n = len(words)
        if n == 0:
            return []
        pos = 0
        left = 0
        charlen = 0
        result = []
        while pos < n:
            if charlen + (pos - left) + len(words[pos]) <= maxWidth:
                charlen += len(words[pos])
                pos += 1
            else:
                tmp_data = self.format_data(words[left:pos], charlen, maxWidth, False)
                left = pos
                charlen = 0
                result.append(tmp_data)
        if charlen:
            tmp_data = self.format_data(words[left:], charlen, maxWidth, True)
            result.append(tmp_data)
        return result