class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(' || c == '[' || c == '{') stack.push(c);

            if ((c == ')' || c == ']' || c == '}') && stack.empty()) return false;

            if (c == ')') {
                char top = stack.pop();
                if (top != '(') return false;
            }
            if (c == ']') {
                char top = stack.pop();
                if (top != '[') return false;
            }
            if (c == '}') {
                char top = stack.pop();
                if (top != '{') return false;
            }
        }

        return stack.empty();
    }
}
