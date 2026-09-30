class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {} # key: {remainder, minCoinIndex}, value: amountOfCoins
        n = len(coins)

        def dfs(remainder, minCoin):
            # print(remainder)
            if (remainder, minCoin) in dp:
                return dp[(remainder, minCoin)]

            if (remainder < 0):
                return 0

            if (remainder == 0):
                return 1

            if (minCoin >= n):
                return 0

            result = 0
            for i in range(minCoin, n):
                step = 0
                if (remainder - coins[i], i) in dp:
                    step = dp[(remainder - coins[i], i)]
                else:
                    step = dfs(remainder - coins[i], i)
                dp[(remainder - coins[i], i)] = step
                result = result + step

            dp[(remainder, minCoin)] = result
            return result

        return dfs(amount, 0)
                