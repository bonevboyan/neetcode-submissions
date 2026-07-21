class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numsSet = new HashSet<Integer>();

        for (int i = 0; i < nums.length; i++) {
            numsSet.add(nums[i]);
        }

        return nums.length != numsSet.size();
    }
}