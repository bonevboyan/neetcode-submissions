class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        const leftRightHeight = [];

        for (let i = 0; i < height.length; i++) {
            leftRightHeight.push({});
        }

        let maxHeightLeft = 0;
        let maxHeightRight = 0;

        for (let i = 0; i < height.length; i++) {
            leftRightHeight[i].height = height[i];
            leftRightHeight[i].left = maxHeightLeft;

            maxHeightLeft = Math.max(maxHeightLeft, height[i]);
        }

        for (let i = height.length - 1; i >= 0; i--) {
            leftRightHeight[i].right = maxHeightRight;

            maxHeightRight = Math.max(maxHeightRight, height[i]);
        }

        let sum = 0;
        for (let i = 0; i < height.length; i++) {
            sum += Math.max(Math.min(leftRightHeight[i].left, leftRightHeight[i].right) 
                - leftRightHeight[i].height, 0)
        }

        return sum;
    }
}
