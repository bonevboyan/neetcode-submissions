class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(open_count, close_count, current):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                dfs(open_count + 1, close_count, current + '(')
            if close_count < open_count:
                dfs(open_count, close_count + 1, current + ')')

        dfs(0, 0, '')
        return result