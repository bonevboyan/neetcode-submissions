class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let lower = 0;
        let upper = matrix.length * matrix[0].length - 1;

        while (lower <= upper) {
            let index = Math.floor((lower + upper) / 2);

            let item = matrix[Math.floor(index / matrix[0].length)][index % matrix[0].length];

            if (item > target) {
                upper = index - 1;
            } else if (item == target) {
                return true;
            } else if (item < target) {
                lower = index + 1;
            }
        }

        return false;
    }
}
