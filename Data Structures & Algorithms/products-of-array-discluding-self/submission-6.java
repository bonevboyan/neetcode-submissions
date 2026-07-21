class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        int[] result = new int[n];

        int[] prefixProduct = new int[n];
        prefixProduct[0] = 1;

        for (int i = 1; i < n; i++) {
            prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1];
        }

        int[] suffixProduct = new int[n];
        suffixProduct[n - 1] = 1;
        result[n - 1] = prefixProduct[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixProduct[i] = suffixProduct[i + 1] * nums[i + 1];
            result[i] = suffixProduct[i] * prefixProduct[i];
        }

        return result;
    }
}  
