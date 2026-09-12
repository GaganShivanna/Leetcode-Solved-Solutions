class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesum = sum(stones)
        target = (stonesum + 1) // 2
        memo = {}
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stonesum - total))
            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i,total)] = min(dfs(i + 1, total + stones[i]), dfs(i + 1, total))
            return memo[(i, total)]
        return dfs(0,0)