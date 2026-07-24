class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        const res = [];
        res[0] = nums[0];
        res[1] = Math.max(nums[0], nums[1]);


        for (let i = 2; i < nums.length; i++) {
            const current = nums[i];
            res[i] = Math.max(current + res[i - 2], res[i - 1]);
        }

        return res[nums.length - 1];
    }
}
