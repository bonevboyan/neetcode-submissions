class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let lowestPrice = prices[0];
        let maxProfit = 0;

        for (let i = 1; i < prices.length; i++) {
            lowestPrice = Math.min(prices[i - 1], lowestPrice)
            maxProfit = Math.max(maxProfit, prices[i] - lowestPrice)
        }

        return maxProfit;
    }
}
