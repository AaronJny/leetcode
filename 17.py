class Solution:
    combinations = []

    digits_chr_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    tmp_chrs = []

    def dfs(self, digits, pos, n):
        if pos >= n:
            self.combinations.append(''.join(self.tmp_chrs))
        else:
            num = digits[pos]
            chrs = self.digits_chr_map.get(num)
            for chr in chrs:
                self.tmp_chrs.append(chr)
                self.dfs(digits, pos + 1, n)
                self.tmp_chrs.pop()

    def letterCombinations(self, digits: str):
        self.combinations.clear()
        self.tmp_chrs.clear()
        if len(digits) == 0:
            return []
        self.dfs(digits, 0, len(digits))
        return list(self.combinations)