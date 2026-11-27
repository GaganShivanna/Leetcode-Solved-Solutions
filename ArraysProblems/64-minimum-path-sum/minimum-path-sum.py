class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[-1] * N for i in range(M)]
        def dfs(i, j):
            if i >= M or j>=N:
                return float('inf')
            if i ==(M - 1) and j == (N - 1):
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = grid[i][j] + min(dfs(i, j + 1), dfs(i + 1, j))
            return dp[i][j]
        return dfs(0,0)
        # BOTTOM - UP APPROACH
        #Convert the recursive dfs(i,j) states into dp[i][j]
        #Convert the recursion into the dp as well
        #the direction is very important, incase the solution currently mentions can only move 
        #for i in range(M - 1, -1, -1):
        #   for j in range(N - 1, -1, -1):
        #       if i == ( M - 1 ) and j == ( N - 1 ):
        #           dp[i][j] = grid[i][j]
        #       elif i == M - 1:
        #           dp[i][j] = grid[i][j] + grid[i][j + 1]
        #       elif j == N - 1:
        #           dp[i][j] = grid[i][j] + grid[i + 1][j]
        #       else:
        #           dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])
        #return dp[0][0]
