#122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr=0
        buy=prices[0]
        for i in prices:
            if i<buy:
                buy=i
            elif (i-buy)>0:
                pr+=i-buy
                buy=i
        return pr     
