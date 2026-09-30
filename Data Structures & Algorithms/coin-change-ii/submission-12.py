class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {} # key: {remainder, minCoinIndex}, value: amountOfCoins
        n = len(coins)

        def dfs(remainder, minCoin):
            if (remainder < 0):
                return 0

            if (remainder == 0):
                return 1

            if (minCoin >= n):
                return 0

            if (remainder, minCoin) in dp:   
                return dp[(remainder, minCoin)]

            step1 = dfs(remainder - coins[minCoin], minCoin)
            step2 = dfs(remainder, minCoin + 1)

            result = step1 + step2

            dp[(remainder, minCoin)] = result
            return result

        return dfs(amount, 0)
                