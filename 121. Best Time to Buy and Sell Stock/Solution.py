class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cost = prices[0]
        profit = 0
        for p in prices:
            if (cost > p):
                cost = p
            elif (p - cost > profit):
                profit = p - cost
        return profit