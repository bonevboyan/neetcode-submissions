class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const count = {};  // frequency of each character in the current window
        let maxCount = 0;  // count of the most frequent character in the window
        let left = 0;
        let maxLength = 0;

        for (let right = 0; right < s.length; right++) {
            const char = s[right];
            count[char] = (count[char] || 0) + 1;

            // track the highest frequency we've seen in any window so far
            maxCount = Math.max(maxCount, count[char]);

            // window size is (right - left + 1)
            // "bad" characters we'd need to replace = window size - maxCount
            // if that's more than k, shrink the window from the left
            if ((right - left + 1) - maxCount > k) {
                count[s[left]]--;
                left++;
            }

            // window is always valid here, so update the answer
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;

    }
}
