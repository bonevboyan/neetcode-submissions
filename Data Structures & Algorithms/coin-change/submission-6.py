class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                # if i % coin == 0:
                #     dp[i] = min(dp[i], i // coin)

        

        if dp[amount] > amount:
            return -1
        return dp[amount]

