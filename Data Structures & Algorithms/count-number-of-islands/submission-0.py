class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        explored = set()

        
        def dfs(i, j):
            if (i, j) not in explored:
                explored.add((i, j))
        
            if i + 1 < len(grid) and grid[i + 1][j] == '1':
                if (i + 1, j) not in explored:
                    dfs(i + 1, j)

            if i - 1 >= 0 and grid[i - 1][j] == '1':
                if (i - 1, j) not in explored:
                    dfs(i - 1, j)
            
            if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':
                if (i, j + 1) not in explored:
                    dfs(i, j + 1)

            if j - 1 >= 0 and grid[i][j - 1] == '1':
                if (i, j - 1) not in explored:
                    dfs(i, j - 1)

            return
                


        count = 0
        for iIndex in range(len(grid)):
            for jIndex in range(len(grid[0])):
                el = grid[iIndex][jIndex]

                if (iIndex, jIndex) not in explored and el == '1':
                    dfs(iIndex, jIndex)
                    count = count + 1

        return count

        
        