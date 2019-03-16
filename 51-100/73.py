class Solution:
    def mark(self, row, col, row_mark, col_mark, matrix, n, m):
        if row_mark[row] == 0:
            row_mark[row] = 1
            for i in range(m):
                matrix[row][i] = 0
        if col_mark[col] == 0:
            col_mark[col] = 1
            for i in range(n):
                matrix[i][col] = 0

    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return
        m = len(matrix[0])
        if m == 0:
            return
        row_mark = [0 for _ in range(n)]
        col_mark = [0 for _ in range(m)]
        zeroes = []
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    zeroes.append((row, col))
        for row, col in zeroes:
            self.mark(row, col, row_mark, col_mark, matrix, n, m)
