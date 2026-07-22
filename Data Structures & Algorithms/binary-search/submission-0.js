class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let lower = 0;
        let upper = nums.length - 1;

        while (lower <= upper) {
            let index = Math.floor((lower + upper) / 2);

            let item = nums[index];

            if (item > target) {
                upper = index - 1;
            } else if (item == target) {
                return index;
            } else if (item < target) {
                lower = index + 1;
            }
        }

        return -1;
    }
}
