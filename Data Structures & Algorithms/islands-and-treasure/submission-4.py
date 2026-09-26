class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    
        depth = 0
        visited = [[0 for x in range(len(grid[0]))] for y in range(len(grid))] 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    visited[i][j] = 1

        while len(queue) != 0:
            currLevel = []
             
            while len(queue) != 0:
                currLevel.append(queue.pop())

            nextLevel = []

            for n in currLevel:
                i = n[0]
                j = n[1]

                grid[i][j] = min(grid[i][j], depth)
                

                if i + 1 < len(grid) and visited[i + 1][j] == 0:
                    visited[i + 1][j] = 1
                    queue.append((i + 1, j))
                
                if j + 1 < len(grid[0]) and visited[i][j + 1] == 0:
                    visited[i][j + 1] = 1
                    queue.append((i, j + 1))

                if i - 1 >= 0 and (i - 1, j) and visited[i - 1][j] == 0:
                    visited[i - 1][j] = 1
                    queue.append((i - 1, j))

                if j - 1 >= 0 and (i, j - 1) and visited[i][j - 1] == 0:
                    visited[i][j - 1] = 1
                    queue.append((i, j - 1))


            depth = depth + 1


            

        