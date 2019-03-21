class Solution:
    def getRow(self, rowIndex: int):
        rowIndex += 1
        if rowIndex == 1:
            return [1]
        last_rows = [1, ]
        for row in range(1, rowIndex):
            tmps = [last_rows[0]]
            for col in range(1, row):
                tmps.append(last_rows[col - 1] + last_rows[col])
            tmps.append(last_rows[-1])
            del last_rows
            last_rows = tmps.copy()
            del tmps
        return last_rows
