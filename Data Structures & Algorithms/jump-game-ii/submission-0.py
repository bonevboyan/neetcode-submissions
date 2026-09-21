class Solution:
    def jump(self, nums: List[int]) -> int:
        proc = [-1] * len(nums)
        for idx, num in enumerate(nums):
            count = num

            if (count + idx) >= len(nums):
                count = len(nums) - idx - 1

            print(count, idx)

            while count > 0 :
                if proc[idx + count] == -1:
                    proc[idx + count] = idx
                count = count - 1


        index = len(nums) - 1
        count = 0
        while index >= 0:
            index = proc[index]
            count = count + 1

        return count - 1

            
        
        