class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        if (s.length == 0) return 0;
        
        const map = new Map();

        let left = 0
        let right = 0

        let longest = 0

        for (let i = 0; i < s.length; i++) {
            const ch = s.charAt(i);
            if (map.has(ch) && map.get(ch) >= left) {
                left = map.get(ch) + 1;
                map.set(ch, i);
            } else {
                map.set(ch, i);
                right = i;
            }

            if (right - left > longest) {
                longest = right - left
            } 
        }

        return longest + 1;
    }
}
