class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            best_length = 1
            count = 1

            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    next_length, next_count = dfs(j)

                    candidate_length = 1 + next_length

                    if candidate_length > best_length:
                        best_length = candidate_length
                        count = next_count

                    elif candidate_length == best_length:
                        count += next_count
            memo[i] = (best_length, count)
            return memo[i]
        
        overall_length = 0
        overall_count = 0
        for i in range(n):
            length, count = dfs(i)
            if length > overall_length:
                overall_length = length
                overall_count = count
            elif length == overall_length:
                overall_count += count
        return overall_count
