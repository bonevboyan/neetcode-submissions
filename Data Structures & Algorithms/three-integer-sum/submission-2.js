class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b);
        const result = [];
        const n = nums.length;

        for (let i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] === nums[i - 1]) continue; // skip duplicate anchors

            let left = i + 1;
            let right = n - 1;
            const target = -nums[i];

            while (left < right) {
                const sum = nums[left] + nums[right];
                if (sum === target) {
                    result.push([nums[i], nums[left], nums[right]]);
                    left++;
                    right--;
                    while (left < right && nums[left] === nums[left - 1]) left++;   // skip duplicate left
                    while (left < right && nums[right] === nums[right + 1]) right--; // skip duplicate right
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }
}
