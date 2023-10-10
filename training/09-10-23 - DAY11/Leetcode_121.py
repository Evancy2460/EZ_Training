#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr=0
        buy=prices[0]
        for i in prices:
            if i<buy:
                buy=i
            elif (i-buy)>pr:
                pr=i-buy
        return pr
        
