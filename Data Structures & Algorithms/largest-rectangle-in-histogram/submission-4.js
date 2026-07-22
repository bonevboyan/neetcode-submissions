class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    largestRectangleArea(heights) {
        const n = heights.length;
        const stack = [];

        stack.push(
        { 
            height: heights[0], 
            index: 0
        });

        let maxArea = 0; 

        for (let i = 1; i < n; i++) {
            const currentHeight = heights[i];
            let currentTop = stack[stack.length - 1]

            while (stack.length > 0 && stack[stack.length - 1].height > currentHeight) {
                const popped = stack.pop();
                const width = stack.length === 0 ? i : i - stack[stack.length - 1].index - 1;
                const currentArea = popped.height * width;
                if (currentArea > maxArea) {
                    maxArea = currentArea;
                }


                
            }

            stack.push(
            { 
                height: heights[i], 
                index: i
            });
        }

            


        while (stack.length > 0) {
            const popped = stack.pop();
            const width = stack.length === 0 ? n : n - stack[stack.length - 1].index - 1;
            const currentArea = popped.height * width;
            if (currentArea > maxArea) maxArea = currentArea;
        }


        return maxArea;
    }
}
