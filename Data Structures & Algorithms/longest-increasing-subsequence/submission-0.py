class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [(0, 0)] * len(nums)
        dp[0] = (1, nums[0])

        for i in range(1, len(nums)):
            current = nums[i]
            maxLen = 1
            maxIndex = 0
            for j in range(0, i):
                if dp[j][1] < current and dp[j][0] + 1 > maxLen:
                    maxLen = dp[j][0] + 1
                    maxIndex = j
            dp[i] = (maxLen, current)

        print(dp)

        return max(dp)[0]

