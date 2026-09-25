class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(openC, closedC, current):
            if len(current) == 2*n:
                result.append(current)
                return

            if openC < n:
                dfs(openC + 1, closedC, current + '(')
            if openC > closedC:
                dfs(openC, closedC + 1, current + ')')

        dfs(0, 0, '')

        return result