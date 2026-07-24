class Solution {
    rob(nums) {
        const n = nums.length;
        if (n === 1) return nums[0];
        if (n === 2) return Math.max(nums[0], nums[1]);

        const robLinear = (arr) => {
            let prev2 = 0, prev1 = 0;
            for (const num of arr) {
                const current = Math.max(num + prev2, prev1);
                prev2 = prev1;
                prev1 = current;
            }
            return prev1;
        };

        return Math.max(
            robLinear(nums.slice(0, n - 1)),
            robLinear(nums.slice(1))
        );
    }
}