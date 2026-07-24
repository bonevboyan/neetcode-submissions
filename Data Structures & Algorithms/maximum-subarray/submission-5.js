class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let currSum = nums[0];
        let bestSum = nums[0];

        for (let i = 1; i < nums.length; i++) {
            const potentialSum = currSum + nums[i];


            if (nums[i] > potentialSum) {
                currSum = nums[i];
            } else {
                currSum = potentialSum;
            }
            console.log(currSum)

            bestSum = Math.max(currSum, bestSum)
        }
        
        return bestSum;
    }
}
