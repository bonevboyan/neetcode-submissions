class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    numDecodings(s) {
        const arr = new Array(s.length + 1).fill(0);

        if (s.charAt(0) == '0') return 0;
        arr[0] = 1;
        arr[1] = 1;

        for (let i = 2; i <= s.length; i++) {
            const first = s.charAt(i - 1);
            const second = s.substring(i - 2, i);

            if (first !== '0') {
                arr[i] += arr[i - 1];
            }
            if (second >= '10' && second <= '26') {
                arr[i] += arr[i - 2];
            }

        }

        console.log(arr)

        return arr[s.length];
    }
}
