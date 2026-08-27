class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M,N = len(grid), len(grid[0])
        dp = [[-1]* N for i in range(M)]
        def dfs(i,j):
            if i>= M or j>=N:
                return 0
            if grid[i][j] == 1:
                return 0
            if i == (M - 1) and j == (N - 1):
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i + 1,j) + dfs(i, j + 1)
            return dp[i][j]
        return dfs(0,0)