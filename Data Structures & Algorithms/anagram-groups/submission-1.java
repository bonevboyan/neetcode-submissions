class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> mappings = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            String toSort = strs[i];
            char[] charsToSort = toSort.toCharArray();
            Arrays.sort(charsToSort);
            String sorted = new String(charsToSort);


            if (mappings.containsKey(sorted)) {
                mappings.get(sorted).add(toSort);
            } else {
                List<String> toAdd = new ArrayList<String>();
                toAdd.add(toSort);
                mappings.put(sorted, toAdd);
            }
        }

        return new ArrayList<>(mappings.values());
    }
}
