class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let n = heights.length;

        let left = 0;
        let right = n - 1;

        let maxAmount = 0;

        while (right > left) {
            const leftH = heights[left]; 
            const rightH = heights[right];
            const smallerH = Math.min(leftH, rightH);

            let currentAmount = Math.abs(right - left) * (smallerH);

            maxAmount = Math.max(currentAmount, maxAmount);

            if (leftH > rightH) {
                right--;
            } else {
                left++;
            }
        }

        return maxAmount;
    }
}
