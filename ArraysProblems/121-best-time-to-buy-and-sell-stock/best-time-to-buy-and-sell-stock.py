class Solution:
    def maxProfit(self, price: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        while r < len(price):
            if price[l] < price[r]:
                profit = max(profit, price[r] - price[l])
            else:
                l = r
            r += 1
        return profit
