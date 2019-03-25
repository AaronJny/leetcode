class Solution:
    def dfs(self, board, not_replace, row, col, n, m):
        if board[row][col] == 'X' or not_replace[row][col]:
            return
        not_replace[row][col] = True
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'O' and (not not_replace[nx][ny]):
                self.dfs(board, not_replace, nx, ny, n, m)

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        if m == 0:
            return
        not_replace = [[False for _ in range(m)] for _ in range(n)]
        for row in range(n):
            self.dfs(board, not_replace, row, 0, n, m)
            self.dfs(board, not_replace, row, m - 1, n, m)
        for col in range(m):
            self.dfs(board, not_replace, 0, col, n, m)
            self.dfs(board, not_replace, n - 1, col, n, m)
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O' and (not not_replace[row][col]):
                    board[row][col] = 'X'
