class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0 
        l = 0
        minsub = float('inf')

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                minsub = min(minsub, r - l + 1)
                curr_sum -= nums[l]
                l+= 1
        return 0 if minsub == float('inf') else minsub