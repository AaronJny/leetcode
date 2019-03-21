class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1], ]
        for row in range(1, numRows):
            tmps = [result[row - 1][0]]
            for col in range(1, row):
                tmps.append(result[row - 1][col - 1] + result[row - 1][col])
            tmps.append(result[row - 1][-1])
            result.append(tmps)
        return result