class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        memo = {}
        def dfs(i,j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if nums1[i] == nums2[j]:
                memo[(i,j)] = 1 + dfs(i + 1, j + 1)
            else:
                memo[(i,j)] = max(dfs(i,j + 1), dfs(i + 1, j))
            return memo[(i,j)]
        return dfs(0,0)