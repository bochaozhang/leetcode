# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l <= 1:
            return
        Max = 0
        Min = prices[0]
        for i in range(1,l):
            Max = max(Max, prices[i]-Min)
            Min = min(Min, prices[i])

        return Max

if __name__ == "__main__":
    prices = [1,2,3,5,6,8,4,10,5,21]
    print Solution().maxProfit(prices)
    prices = []
    print Solution().maxProfit(prices)
