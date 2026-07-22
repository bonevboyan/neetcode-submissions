class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let n = nums.length;

    let min = 0;
    let max = n - 1;

    while (min <= max) {
        let guessRotations = Math.floor(min + (max - min) / 2);

        let guess = nums[guessRotations];
        let afterGuess = nums[guessRotations + 1];

        if (guessRotations > 0) {
            let beforeGuess = nums[guessRotations - 1];
            if (beforeGuess > guess) {
                return guess;
            }
        }
        
        if (afterGuess < guess) {
            return afterGuess;
        } else {
            let first = nums[min];
            let last = nums[max];

            if (guess > last) {
                min = guessRotations + 1;
            } else if (guess < first) {
                max = guessRotations - 1;
            } else {
                return first;
            }
        }
    }

    return nums[min]
    }
}
