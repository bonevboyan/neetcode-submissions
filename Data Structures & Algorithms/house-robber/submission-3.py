class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        result = [0] * n
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])

        for i in range(2, n):
            result[i] = max(result[i - 1], result[i - 2] + nums[i])

        return result[n - 1]

        