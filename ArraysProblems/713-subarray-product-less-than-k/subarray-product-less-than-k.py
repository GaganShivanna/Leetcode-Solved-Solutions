class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        totalcount = 0
        product = 1
        l = 0
        for r, num in enumerate(nums):
            product *= num
            while product >= k:
                product //= nums[l]
                l += 1
            totalcount += r - l + 1
        return totalcount