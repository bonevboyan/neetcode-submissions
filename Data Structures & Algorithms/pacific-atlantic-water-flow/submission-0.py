class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificFront = []
        atlanticFront = []

        # visits = ([0] * ) * len(heights)
        visits = [[0 for x in range(len(heights[0]))] for y in range(len(heights))] 


        for idx in range(len(heights)):
            for jdx in range(len(heights[0])):
                if (idx == 0 or jdx == 0):
                    pacificFront.append((idx, jdx))
                    visits[idx][jdx] = visits[idx][jdx] + 3

                if (idx == len(heights) - 1 or jdx == len(heights[0]) - 1):
                    atlanticFront.append((idx, jdx))
                    visits[idx][jdx] = visits[idx][jdx] + 7
        # for idx in range(len(heights)):
        #     # print 
            
            
        #     atlanticFront.append((idx, len(heights[0]) - 1))
        #     visits[idx][len(heights[0]) - 1] = 7

        # for idx in range(len(heights[0])):
        #     pacificFront.append((0, idx))
        #     visits[0][idx] = 3
        #     atlanticFront.append((len(heights) - 1, idx))
        #     visits[len(heights) - 1][idx] = 7

        print(atlanticFront)
        print(pacificFront)
            

        while len(pacificFront) != 0:
            current = pacificFront.pop()

            i = current[0]
            j = current[1]

            currentVal = heights[i][j]

            if i + 1 < len(heights) and visits[i + 1][j] != 3 and visits[i + 1][j] != 10 and heights[i + 1][j] >= currentVal:
                visits[i + 1][j] = visits[i + 1][j] + 3
                pacificFront.append((i + 1, j))

            if j + 1 < len(heights[0]) and visits[i][j + 1] != 3 and visits[i][j + 1] != 10 and heights[i][j + 1] >= currentVal:
                visits[i][j + 1] = visits[i][j + 1] + 3
                pacificFront.append((i, j + 1))

            if i - 1 >= 0 and visits[i - 1][j] != 3 and visits[i - 1][j] != 10 and heights[i - 1][j] >= currentVal:
                visits[i - 1][j] = visits[i - 1][j] + 3
                pacificFront.append((i - 1, j))

            if j - 1 >= 0 and visits[i][j - 1] != 3 and visits[i][j - 1] != 10 and heights[i][j - 1] >= currentVal:
                visits[i][j - 1] = visits[i][j - 1] + 3
                pacificFront.append((i, j - 1))

        while len(atlanticFront) != 0:
            current = atlanticFront.pop()

            i = current[0]
            j = current[1]

            currentVal = heights[i][j]

            if i + 1 < len(heights) and visits[i + 1][j] != 7 and visits[i + 1][j] != 10 and heights[i + 1][j] >= currentVal:
                visits[i + 1][j] = visits[i + 1][j] + 7
                atlanticFront.append((i + 1, j))

            if j + 1 < len(heights[0]) and visits[i][j + 1] != 7 and visits[i][j + 1] != 10 and heights[i][j + 1] >= currentVal:
                visits[i][j + 1] = visits[i][j + 1] + 7
                atlanticFront.append((i, j + 1))

            if i - 1 >= 0 and visits[i - 1][j] != 7 and visits[i - 1][j] != 10 and heights[i - 1][j] >= currentVal:
                visits[i - 1][j] = visits[i - 1][j] + 7
                atlanticFront.append((i - 1, j))

            if j - 1 >= 0 and visits[i][j - 1] != 7 and visits[i][j - 1] != 10 and heights[i][j - 1] >= currentVal:
                visits[i][j - 1] = visits[i][j - 1] + 7
                atlanticFront.append((i, j - 1))

        result = []
        for i in range(len(visits)):
            for j in range(len(visits[0])):
                if visits[i][j] == 10:
                    result.append([i, j])


        return result


        