## buy stock version 1 - at most once
class Solution_1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        else:
            profit = 0
            curr_min = prices[0]
            for i in range(0,len(prices)):
                profit = max(profit, prices[i] - curr_min)
                curr_min = min(curr_min, prices[i])

            return profit

## BUY stock version 2 - as many as you want
class Solution_2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        else:
            profit = 0
            for i in range(1,len(prices)):
                profit +=  prices[i] - prices[i-1] if prices[i] - prices[i-1] >0 else 0
            return profit

## BUY stock version 3 - at most 2 transactions
class Solution_3(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        key: to construct two array f[i], g[j]
             f[i] - profit for [0....i] days
             g[j] - profit for [i+1....n-1] days
        """
        n = len(prices)
        if n < 2:
            return 0
        else:
            f = [0] * n
            g = [0] * n
            f_min = prices[0]
            g_max = prices[-1]
            f_profit = g_profit = 0
            max_profit = 0

            for i in range(0, n):
                f_min = min(f_min, prices[i]) # here the order doesnt really matter, as if its min, profit will be unchanged
                f_profit = max(f_profit, prices[i] - f_min)
                f[i] = f_profit

            for j in range(n-1,0,-1):
                g_max = max(g_max, prices[j])
                g_profit = max(g_profit, g_max - prices[j])
                g[j] = g_profit

            for i in range(0, n):
                max_profit = max(max_profit, f[i] + g[i])
            return max_profit

## at most k times
class Solution_4(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        THE FOLLOWING IS being referenced
        http://bookshadow.com/weblog/2015/02/18/leetcode-best-time-to-buy-and-sell-stock-iv/
        """

        size = len(prices)
        if k > size/2:
            profit = 0
            # case where k is too big
            for i in range(1,size):
                profit += prices[i] - prices[i-1] if prices[i] - prices[i-1] > 0 else 0
            return profit
        else:
            # case where k is reasonably small
            dp = [None] * (2*k + 1)
            dp[0] = 0

            for i in range(size):
                for j in range(min(2*k,i+1), 0, -1):
                    dp[j] = max(dp[j], dp[j-1] + prices[i] * [1, -1][j % 2])

            return max(dp)

## case where there is a cool down of 1 day
class Solution_5(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size < 2:
            return 0
        buys = [None] * size
        sells = [None] * size
        buys[0] = -prices[0]
        buys[1] = max(-prices[0], -prices[1])
        sells[0] = 0
        sells[1] = max(0, prices[1] - prices[0])

        for x in range(2, size):
            sells[x] = max(sells[x - 1], buys[x - 1] + prices[x])
            buys[x] = max(buys[x - 1], sells[x - 2] - prices[x])
        return sells[-1]