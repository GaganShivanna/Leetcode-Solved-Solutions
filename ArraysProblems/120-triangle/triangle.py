class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dfs(r, c):
            if r>= len(triangle):
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)] = triangle[r][c] + min(dfs(r + 1, c), dfs(r + 1, c + 1))
            return memo[(r,c)]
        return dfs(0,0)