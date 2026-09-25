class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        current = nums.copy()

        def dfs(idx, history):
            # print('curr', current)
            # print('his', history)
            if len(current) == 0:
                # print('history', history)
                result.append(history.copy())

            for i, num in enumerate(current):
                # if idx > i:
                #     continue
                current.remove(num)
                dfs(i, history + [num])
                current.insert(i, num)
                # dfs(i, history)

        dfs(0, [])

        return result
        