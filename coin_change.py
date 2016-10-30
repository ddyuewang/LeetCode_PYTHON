class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        ### The DP equation: dp[i] = min(dp[i - coins[j]]+1, dp[i])
        """
        # dp = [0] + [amount + 1] * amount
        # for i in range(1, amount+1):
        #     for j in range(len(coins)):
        #         if coins[j] <= i and dp[i-coins[j]] != amount + 1:
        #             dp[i] = min(dp[i-coins[j]] + 1, dp[i])
        # if dp[amount] == amount + 1:
        #     return -1
        # return dp[amount]

        dp = [0] + [-1] * amount
        for x in range(amount):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                    dp[x + c] = dp[x] + 1
        return dp[amount]