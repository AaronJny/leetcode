class Solution:
    ok = False
    row_check = []
    col_check = []
    block_check = []

    def check(self, row, col, num):
        """
        检查是否可以在数独板的第row行第col列填写num
        :param row:
        :param col:
        :param num:
        :return:
        """
        if num in self.row_check[row]:
            return False
        if num in self.col_check[col]:
            return False
        if num in self.block_check[int(row / 3)][int(col / 3)]:
            return False
        return True

    def mark(self, row, col, num, board):
        """
        在board[row][col]上填上num，并在去重器上标记
        :param row: 行号
        :param col: 列号
        :param num: 要填的数字
        :param board: 数独板
        :return:
        """
        self.row_check[row].add(num)
        self.col_check[col].add(num)
        self.block_check[int(row / 3)][int(col / 3)].add(num)
        board[row][col] = num

    def unmark(self, row, col, num, board):
        """
        取消在数独板row,col位置的填写操作
        :param row:
        :param col:
        :param num:
        :param board:
        :return:
        """
        self.row_check[row].remove(num)
        self.col_check[col].remove(num)
        self.block_check[int(row / 3)][int(col / 3)].remove(num)
        board[row][col] = '.'

    def dfs(self, board, row, col, board_size):
        """
        使用深搜+回溯尝试数独的做法
        :param board:
        :param row:
        :param col:
        :param board_size:
        :return:
        """
        if self.ok:
            return
        if row >= board_size:
            self.ok = True
            return
        if board[row][col] == '.':
            for i in range(1, 10):
                num = str(i)
                if self.check(row, col, num):
                    next_col = col + 1
                    next_row = row
                    if next_col >= board_size:
                        next_row = row + 1
                        next_col = 0
                    self.mark(row, col, num, board)
                    self.dfs(board, next_row, next_col, board_size)
                    if self.ok:
                        return
                    else:
                        self.unmark(row, col, num, board)
        else:
            next_col = col + 1
            next_row = row
            if next_col >= board_size:
                next_row = row + 1
                next_col = 0
            self.dfs(board, next_row, next_col, board_size)

    def init_board(self, board, board_size):
        """
        根据给定的数独板，在行、列、3*3小方块上标记好，
        减少深搜时的计算量
        :param board: 数独板
        :param board_size: 数独尺寸
        :return:
        """
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] != ".":
                    self.mark(row, col, board[row][col], board)

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_size = len(board)
        # 初始化数据结构
        self.ok = False
        self.row_check = [set() for _ in range(board_size)]
        self.col_check = [set() for _ in range(board_size)]
        self.block_check = []
        for i in range(int(board_size / 3)):
            tmps = [set() for _ in range(int(board_size / 3))]
            self.block_check.append(tmps)
        # 根据数独板预填去重器，减少计算量
        self.init_board(board, board_size)
        # 深搜+回溯查找结果
        self.dfs(board, 0, 0, board_size)
        # 清理内存
        del self.row_check
        del self.col_check
        del self.block_check
