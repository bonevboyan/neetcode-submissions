class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (hashMap.containsKey(target - nums[i])) {
                int[] result = {hashMap.get(target- nums[i]), i};
                return result;
            }
            hashMap.put(nums[i], i);
        }

        int[] result = {0, 1};
        return result;
    }
}
