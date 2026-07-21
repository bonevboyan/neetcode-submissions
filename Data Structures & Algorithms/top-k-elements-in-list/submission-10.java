class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> countersPerNumber = new HashMap<>();

        int biggestCount = 1;

        for (int i = 0; i < nums.length; i++) {
            if (countersPerNumber.containsKey(nums[i])) {
                int newCount = countersPerNumber.get(nums[i]) + 1;
                countersPerNumber.put(nums[i], newCount);
                if (newCount > biggestCount) {
                    biggestCount = newCount;
                }
            } else {
                countersPerNumber.put(nums[i], 1);
            }
        }

        ArrayList<Integer>[] buckets = new ArrayList[biggestCount + 1];

        for (int n: countersPerNumber.keySet()) {
            ArrayList<Integer> list = buckets[countersPerNumber.get(n)];

            if (list == null) {
                buckets[countersPerNumber.get(n)] = new ArrayList<Integer>();
            }

            buckets[countersPerNumber.get(n)].add(n);
        }

        int[] result = new int[k];
        int index = 0;
        int currentBucket = biggestCount;

        for (int i = 0; i < k; i++) {
            ArrayList<Integer> bucketList = buckets[currentBucket];

            while (bucketList == null || bucketList.size() <= index) {
                currentBucket--;
                bucketList = buckets[currentBucket];
                index = 0;
            }


            result[i] = bucketList.get(index);
            index++;
        }
        return result;
    }
}
