class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        resultNoEnd = [0] * n
        resultNoEnd[0] = nums[0]
        resultNoEnd[1] = max(nums[1], nums[0])

        resultNo1 = [0] * n
        resultNo1[0] = 0
        resultNo1[1] = nums[1]

        for i in range(2, n):
            resultNoEnd[i] = max(resultNoEnd[i - 1], resultNoEnd[i - 2] + nums[i])
            resultNo1[i] = max(resultNo1[i - 1], resultNo1[i - 2] + nums[i])

        return max(resultNoEnd[n - 2],  resultNo1[n-1])

        