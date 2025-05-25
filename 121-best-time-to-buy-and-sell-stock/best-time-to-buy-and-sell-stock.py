class Solution(object):
    def maxProfit(self, prices):
        l,r = 0,0
        maxP=0
        while r < len(prices):
            if prices[l] < prices[r]:
                Profit = prices[r] - prices[l]
                maxP = max(maxP , Profit)
            else:
                l = r 
            r+=1
        return maxP