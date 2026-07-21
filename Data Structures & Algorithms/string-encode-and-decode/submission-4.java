class Solution {

    public String encode(List<String> strs) {
        List<String> fixed = strs.stream().map(x -> {
            if (x.isEmpty()) {
                return "999WHITESPACE888";
            }
            return x;
        }).toList();;
        String result = String.join("000SEPARATOR111", fixed);

        return result;
    }

    public List<String> decode(String str) {
        if (str.length() == 0) return new ArrayList<String>();
        List<String> list = new ArrayList<String>(Arrays.asList(str.split("000SEPARATOR111")));

        return list.stream().map(x -> {
            if (x.equals("999WHITESPACE888")) {
                return "";
            }
            return x;
        }).toList();
    }
}
