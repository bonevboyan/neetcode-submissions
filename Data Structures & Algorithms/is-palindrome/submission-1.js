function isCorrectChars(c) {
    return (c >= 'a' && c <= 'z' || c >= '0' && c <= '9');
}

class Solution {
    
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const lowercase = s.toLowerCase();

        let left = 0;
        let right = s.length - 1;
        while (left < right) {
            while (!isCorrectChars(lowercase.charAt(left)) && left <= right) {
                left++;
            }
            while (!isCorrectChars(lowercase.charAt(right)) && left <= right) {
                right--;
            }

            if (left > right) return true;

            let leftChar = lowercase.charAt(left);
            let rightChar = lowercase.charAt(right);

            if (leftChar != rightChar) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
