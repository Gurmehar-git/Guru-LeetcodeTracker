# Runtime: 284 ms
# Memory: 19.6 MB

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[[-1]*(k+1) for _ in range(2)] for _ in range(n)]
        def f(i, buy, cap):
            if i == n or cap == 0:
                return 0
            if dp[i][buy][cap] != -1:
                return dp[i][buy][cap]
            if buy == 1:
                take = -prices[i] + f(i+1, 0, cap)
                nottake = f(i+1, 1, cap)
                profit = max(take, nottake)
            else:
                sell = prices[i] + f(i+1, 1, cap-1)
                notsell = f(i+1, 0, cap)
                profit = max(sell, notsell)
            dp[i][buy][cap] = profit
            return profit
        return f(0,1,k)