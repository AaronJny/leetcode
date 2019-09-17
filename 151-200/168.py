import string


class Solution:
    def convertToTitle(self, n: int) -> str:
        num_word_map = {num: word for (num, word) in zip(range(1, 26), string.ascii_uppercase)}
        num_word_map[0] = 'Z'
        words = []
        while n:
            x = n % 26
            words.append(num_word_map[x])
            n = (n - 1) // 26
        return ''.join(words[::-1])