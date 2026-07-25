class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    countSubstrings(s) {
        const n = s.length;

        let count = 0;

        for (let i = 0; i < n; i++) {
            let left = i;
            let right = i;
            while (left >= 0 && right < n) {
                count++;
                left--;
                right++;
                if (s.charAt(left) !== s.charAt(right)) {
                    break;
                }
                
            }
            left = i;
            right = i + 1;
            if (s.charAt(left) != s.charAt(right)) continue;
            while (left >= 0 && right < n) {
                count++;
                left--;
                right++;

                if (s.charAt(left) !== s.charAt(right)) {
                    break;
                }
            }
        }

        return count;
    }
}
