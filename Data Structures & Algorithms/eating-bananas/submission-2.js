class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let max = 0;
        let min = 1;

        for (let i = 0; i < piles.length; i++) {
            max = Math.max(piles[i], max);
            // min = Math.min(piles[i], min);
        }

        let minK = max;

        while (max >= min) {
            let k = Math.floor(max + (min - max) / 2);

            let total = 0;

            for (let i = 0; i < piles.length; i++) {
                total += Math.ceil(piles[i] / k);
            }

            if (total <= h) {
                minK = Math.min(k, minK);
                max = k - 1;
            } else if (total > h) {
                min = k + 1;
            }
        }

        return minK;
    }
}
