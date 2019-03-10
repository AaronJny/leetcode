class Solution:

    def check_valid(self, board, row_start, row_end, col_start, col_end):
        tmpset = set()
        for row in range(row_start, row_end):
            for col in range(col_start, col_end):
                if "." == board[row][col]:
                    continue
                else:
                    if board[row][col] in tmpset:
                        return False
                    else:
                        tmpset.add(board[row][col])
        return True

    def isValidSudoku(self, board) -> bool:
        # 检查行
        board_size = len(board)
        for row in range(board_size):
            flag = self.check_valid(board, row, row + 1, 0, board_size)
            if not flag:
                return flag
        # 检查列
        for col in range(board_size):
            flag = self.check_valid(board, 0, board_size, col, col + 1)
            if not flag:
                return flag
        # 检查方块
        for row in range(0, board_size, 3):
            for col in range(0, board_size, 3):
                flag = self.check_valid(board, row, row + 3, col, col + 3)
                if not flag:
                    return flag
        return True
