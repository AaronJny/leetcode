class Solution:
    def bin_search(self, matrix, target, n, m):
        row_left = 0
        row_right = n - 1

        while row_left <= row_right:
            row_mid = (row_left + row_right) >> 1
            if matrix[row_mid][0] > target:
                row_right = row_mid - 1
            elif matrix[row_mid][-1] < target:
                row_left = row_mid + 1
            else:
                col_left = 0
                col_right = m - 1
                while col_left <= col_right:
                    col_mid = (col_left + col_right) >> 1
                    if matrix[row_mid][col_mid] == target:
                        return row_mid, col_mid
                    elif matrix[row_mid][col_mid] > target:
                        col_right = col_mid - 1
                    else:
                        col_left = col_mid + 1
                break
        return -1, -1

    def searchMatrix(self, matrix, target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        x, y = self.bin_search(matrix, target, n, m)
        if x == -1:
            return False
        else:
            return True
