class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            candidates = (curr, currMax * curr, currMin * curr)

            currMax = max(candidates)
            currMin = min(candidates)

            maximum = max(currMax, maximum)

        return maximum