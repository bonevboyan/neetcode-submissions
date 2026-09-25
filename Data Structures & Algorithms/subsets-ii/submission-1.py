class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        current = []

        def dfs(i):
            if i >= len(nums):
                result.append(current.copy())
                return

            current.append(nums[i])
            dfs(i + 1)

            current.pop()
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i = i + 1
            dfs(i + 1)

        dfs(0)

        return result