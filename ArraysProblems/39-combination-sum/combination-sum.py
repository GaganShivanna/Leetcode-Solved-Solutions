class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or i >= len(candidates):
                return
            #Take
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            #Not Take
            cur.pop()
            dfs(i + 1, cur, total )

        dfs(0, [], 0)
        return res 