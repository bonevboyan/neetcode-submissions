class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> countersPerNumber = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (countersPerNumber.containsKey(nums[i])) {
                countersPerNumber.put(nums[i], countersPerNumber.get(nums[i]) + 1);
            } else {
                countersPerNumber.put(nums[i], 1);
            }
        }

        ArrayList<Map.Entry<Integer, Integer>> res = 
            new ArrayList(countersPerNumber.entrySet());
        res.sort(Map.Entry.comparingByValue());
        Collections.reverse(res);

        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = res.get(i).getKey();
        }

        return result;
    }
}
