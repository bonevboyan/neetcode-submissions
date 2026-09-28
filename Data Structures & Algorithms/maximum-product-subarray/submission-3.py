class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        maxim = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            candidates = (x, x * curMax, x * curMin)
            curMax = max(candidates)
            curMin = min(candidates)

            maxim = max(maxim, curMax)

        return maxim