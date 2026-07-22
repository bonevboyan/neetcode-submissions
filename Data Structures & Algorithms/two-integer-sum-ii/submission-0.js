class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        const n = numbers.length;

        let right = n - 1;
        let left = 0;

        while (right >= left) {
            let leftEl = numbers[left];
            let rightEl = numbers[right];

            if (leftEl + rightEl == target) {
                return [left + 1, right + 1]
            } else if (leftEl + rightEl > target) {
                right--;
            } else {
                left++;
            }
        }

        return []
    }
}
