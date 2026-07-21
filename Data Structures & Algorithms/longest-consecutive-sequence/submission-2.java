class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }
        HashSet<Integer> beginnings = new HashSet<Integer>();

        for (Integer num : set) {
            if (!set.contains(num - 1)) {
                beginnings.add(num);
            }
        }

        int longest = 0;

        for (Integer begin : beginnings) {
            int currentStreak = 1;
            int currentNum = begin;
            set.remove(begin);

            while (set.contains(currentNum + 1)) {
                currentStreak++;
                currentNum++;
                set.remove(currentNum);
            }

            if (currentStreak > longest) {
                longest = currentStreak;
            }
        }

        return longest;
    }
}
