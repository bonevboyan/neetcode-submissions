class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            hashMap.merge(s.charAt(i), 1, (a, b) -> a + b);
        }

        HashMap<Character, Integer> hashMap1 = new HashMap<>();

        for (int i = 0; i < t.length(); i++) {
            hashMap1.merge(t.charAt(i), 1, (a, b) -> a + b);
        }

        return hashMap.equals(hashMap1);
    }
}
