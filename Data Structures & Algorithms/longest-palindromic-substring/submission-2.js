class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    longestPalindrome(s) {
        const n = s.length;
        let maxLeft = 0;
        let maxRight = 0;
        let max = 0;

        for (let i = 0; i < n; i++) {
            let left = i;
            let right = i;
            while (left >= 0 && right < n) {
                if (right - left + 1 > max) {
                    max = Math.max(right - left + 1, max); 
                    maxLeft = left;
                    maxRight = right;
                }
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
                if (right - left + 1 > max) {
                    max = Math.max(right - left + 1, max); 
                    maxLeft = left;
                    maxRight = right;
                }

                left--;
                right++;

                if (s.charAt(left) !== s.charAt(right)) {
                    break;
                }
            }
        }

        return s.substring(maxLeft, maxRight + 1);
    }
}
