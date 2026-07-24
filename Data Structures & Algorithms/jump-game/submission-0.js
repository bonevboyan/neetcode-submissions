class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    canJump(nums) {
        const n = nums.length
        if (n == 1) {
            return true;
        }

        // nums[n - 1] = 1000;
        let indexOfFreedom = n - 1;

        for (let i = n - 1; i >= 0; i--) {
            if (i + nums[i] >= indexOfFreedom) {
                indexOfFreedom = i;
            }
        }
        return indexOfFreedom == 0;
    }
}
