class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        def isOnEdge(i, j):
            if i == 0 or i == len(board) - 1:
                return True

            if j == 0 or j == len(board[0]) - 1:
                return True

            return False

        def bfs(i, j):
            queue = []
            visited = []
            queue.append((i, j))
            visited.append((i, j))
            board[i][j] = 'C'

            isNearEdge = False

            while len(queue) != 0:
                current = queue.pop()

                i = current[0]
                j = current[1]


                # print(i, j)

                if isOnEdge(i, j):
                    isNearEdge = True
                    

                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    r, c = i + di, j + dj

                    if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'O':
                        board[r][c] = 'C'
                        queue.append((r, c))
                        visited.append((r, c))

            if isNearEdge:
                for (i, j) in visited:
                    board[i][j] = 'V'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    bfs(i, j)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'V':
                    board[i][j] = 'O'

                if board[i][j] == 'C':
                    board[i][j] = 'X'



                


                

        