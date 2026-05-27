class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        l = 0
        r = 1
        if prices[r] > prices[l]:
            profit = 

        """
        l = 0
        profit = 0 
        res = 0
        for r in range(1,len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                res = max(profit, res)
            else:
                l = r
        return res

        