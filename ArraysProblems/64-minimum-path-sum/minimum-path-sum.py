class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [ [-1] * N for i in range(M)]
        def dfs(i,j):
            if i >= M or j >= N:
                return float('inf')
            if i == (M - 1) and j == (N - 1):
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = grid[i][j] + min(dfs(i, j + 1), dfs(i + 1, j))
            return dp[i][j]
        return dfs(0,0)