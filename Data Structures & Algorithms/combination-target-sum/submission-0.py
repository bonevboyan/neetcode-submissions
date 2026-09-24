class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        # current = []
        def dfs(nums, target, history, after):
            nonlocal result
            # nonlocal current
            # print(target, current)
            if target == 0:
                result.append(history)

            if target < 0:
                return

            for num in nums:
                if num < after:
                    continue
                newHistory = history + [num]
                # print(current)
                dfs(nums, target - num, newHistory, num)

        dfs(nums, target, [], 0)

        return result 
        