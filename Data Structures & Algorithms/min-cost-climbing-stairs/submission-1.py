class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = [100000] * len(cost)

        result[0] = 0
        result[1] = 0

        for i in range(2, len(cost)):
            result[i] = min(result[i], 
                result[i - 1] + cost[i - 1], 
                result[i - 2] + cost[i - 2])

        print(result)

        return min(result[len(cost) - 1] + cost[len(cost) - 1], result[len(cost) - 2] + cost[len(cost) - 2])
            
            
        