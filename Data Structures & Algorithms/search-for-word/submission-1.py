class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        expr = set()

        height = len(board)
        width = len(board[0])

        flag = False

        def dfs(down, right, currentWord):
            nonlocal flag
            if not word.startswith(currentWord):
                return
            if currentWord == word:
                flag = True
                return

            if down + 1 < height and (down + 1, right) not in expr:
                expr.add((down + 1, right))
                dfs(down + 1, right, currentWord + board[down + 1][right])
                expr.remove((down + 1, right))
            if down - 1 >= 0 and (down - 1, right) not in expr:
                expr.add((down - 1, right))
                dfs(down - 1, right, currentWord + board[down - 1][right])
                expr.remove((down - 1, right))

            if right + 1 < width and (down, right + 1) not in expr:
                expr.add((down, right + 1))
                dfs(down, right + 1, currentWord + board[down][right + 1])
                expr.remove((down, right + 1))

            if right - 1 >= 0 and (down, right - 1) not in expr:
                expr.add((down, right - 1))
                dfs(down, right - 1, currentWord + board[down][right - 1])
                expr.remove((down, right - 1))

        for i in range(height):
            for j in range(width):
                expr = set()
                expr.add((i, j))
                dfs(i, j, board[i][j])

        return flag