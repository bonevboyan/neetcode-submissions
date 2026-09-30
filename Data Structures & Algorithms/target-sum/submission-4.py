class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # key: {remainder, minCoinIndex}, value: amountOfCoins
        n = len(nums)

        def dfs(remainder, index):
            # print(remainder, index)
            if remainder == 0 and index == n:
                return 1

            if (index >= n):
                return 0

            if (remainder, index) in dp:   
                return dp[(remainder, index)]
                
            result = 0

            step1 = dfs(remainder - nums[index], index + 1)
            step2 = dfs(remainder + nums[index], index + 1)

            result = step1 + step2

            dp[(remainder, index)] = result
            return result
        res = dfs(target, 0)

        # print(dp)
        return res