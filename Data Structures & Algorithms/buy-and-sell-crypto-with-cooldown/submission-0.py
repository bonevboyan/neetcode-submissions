class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) 
        dp = {} # key={index, buy},val=maxval 

        def dfs(i, buying):
            if i >= n:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buyCase = dfs(i + 1, False) - prices[i]
                cooldownCase = dfs(i + 1, True)

                dp[(i, buying)] = max(buyCase, cooldownCase)

            else:
                sellCase = dfs(i + 2, True) + prices[i]
                cooldownCase = dfs(i + 1, False)

                dp[(i, buying)] = max(sellCase, cooldownCase)

            return dp[(i, buying)]

        # print(dp)
        return dfs(0, True)