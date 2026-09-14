class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        maxi = 0
        while r < len(prices):
            #profit
            if prices[l] < prices[r]:
                temp = prices[r] - prices[l]
                maxi = max(temp, maxi)
            else:
                l = r
            r +=1

        return maxi
