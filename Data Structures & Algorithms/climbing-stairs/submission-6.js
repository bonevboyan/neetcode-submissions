class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        if(n == 1 || n == 2) return n;

        const result = []
        result[0] = 1;
        result[1] = 2; 

        let index = 2;

        while (result.length != n) {
            result[index] = result[index - 1] + result[index - 2];
            index++;
        }

        return result[n - 1]
    }
}
