class Solution:
    result = False

    def dfs(self, row, col, pos, board, word, used, n, m, z):
        if self.result:
            return
        if pos == z:
            self.result = True
        else:
            dx = [0, 1, 0, -1, 0]
            dy = [0, 0, 1, 0, -1]
            for i in range(5):
                nx = row + dx[i]
                ny = col + dy[i]
                if (not self.result) and 0 <= nx < n and 0 <= ny < m and (not used[nx][ny]) and board[nx][ny] == word[
                    pos]:
                    used[nx][ny] = True
                    self.dfs(nx, ny, pos + 1, board, word, used, n, m, z)
                    used[nx][ny] = False

    def exist(self, board, word: str) -> bool:
        n = len(board)
        if n == 0:
            return False
        m = len(board[0])
        if m == 0:
            return False
        z = len(word)
        if z == 0:
            return False
        used = [[False for i in range(m)] for j in range(n)]
        self.result = False
        for row in range(n):
            for col in range(m):
                self.dfs(row, col, 0, board, word, used, n, m, z)
        return self.result