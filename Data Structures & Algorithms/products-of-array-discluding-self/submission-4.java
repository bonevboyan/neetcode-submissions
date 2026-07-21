class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];

        List<Integer> zeroIndexes = new ArrayList<Integer>();

        int product = 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                product *= nums[i];
            } else {
                zeroIndexes.add(i);
            }
        }

        if (zeroIndexes.size() == 0) {
            for (int i = 0; i < nums.length; i++) {
                result[i] = product / nums[i];
            }
        } else if (zeroIndexes.size() == 1) {
            for (int i = 0; i < nums.length; i++) {
                if (i == zeroIndexes.get(0)) {
                    result[i] = product;
                } else {
                    result[i] = 0;
                }
            }
        } else {
            for (int i = 0; i < nums.length; i++) {
                result[i] = 0;
            }
        }

        return result;
    }
}  
