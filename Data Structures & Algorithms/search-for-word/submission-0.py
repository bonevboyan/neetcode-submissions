class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        expr = set()

        height = len(board)
        width = len(board[0])

        flag = False

        def dfs(down, right, currentWord):
            nonlocal flag                        # FIX 1: otherwise flag = True makes a new local
            if not word.startswith(currentWord): # FIX 2: prune paths that can't become word
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

            if right + 1 < width and (down, right + 1) not in expr:   # FIX 3: width, not height
                expr.add((down, right + 1))
                dfs(down, right + 1, currentWord + board[down][right + 1])
                expr.remove((down, right + 1))

            if right - 1 >= 0 and (down, right - 1) not in expr:
                expr.add((down, right - 1))
                dfs(down, right - 1, currentWord + board[down][right - 1])
                expr.remove((down, right - 1))

        for i in range(height):
            for j in range(width):               # FIX 4: loop over columns, not rows
                expr = set()
                expr.add((i, j))
                dfs(i, j, board[i][j])

        return flag