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
        const resNo1 = [];
        res[0] = {num: nums[0], hasFirst: true};
        res[1] = {num: Math.max(nums[0], nums[1]), hasFirst: nums[0] > nums[1]};
        resNo1[0] = 0;
        resNo1[1] = nums[1];

        for (let i = 2; i < nums.length; i++) {
            const current = nums[i];
            res[i] = { num: Math.max(current + res[i - 2].num, res[i - 1].num), hasFirst: current + res[i - 2].num > res[i - 1].num }
            resNo1[i] = Math.max(current + resNo1[i - 2], resNo1[i - 1]);
        }

        console.log(res)

        let lastNoFirst = 0;
        for (let i = nums.length - 1; i >= 0; i--) {
            if (!res[i].hasFirst) {
                lastNoFirst = res[i].num;
                break;
            }
        }
        if (lastNoFirst == 0) {
            return res[nums.length - 2].num
        }


        if (res[nums.length - 1].hasFirst) {
            return Math.max(lastNoFirst, resNo1[nums.length - 1], res[nums.length - 2].num);
        }
        return res[nums.length - 1].num
    }
}
