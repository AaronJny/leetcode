import string


class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        letter_num_map = {x: y for x, y in zip(string.ascii_uppercase, range(1, 27))}
        for index, x in enumerate(s[::-1]):
            num = letter_num_map.get(x)
            total += num * (26 ** index)
        return total