class Solution:

    def dfs(self, grid, x, y, n, m):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        grid[x][y] = '0'
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
                self.dfs(grid, nx, ny, n, m)

    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, n, m)
                    cnt += 1
        return cnt