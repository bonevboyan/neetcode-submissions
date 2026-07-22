class Solution {
    public int evalRPN(String[] tokens) {
        Collections.reverse(Arrays.asList(tokens));
        Stack<String> stack = new Stack<>();
        for (String token: tokens) {
            stack.push(token);
        }

            Stack<Integer> numbers = new Stack<>();
        while (!stack.empty()) {

            while (!stack.empty() && !stack.peek().equals("*") && !stack.peek().equals("/")
             && !stack.peek().equals("-") && !stack.peek().equals("+")) {
                numbers.push(Integer.parseInt(stack.pop()));
            }

            Integer firstNum = numbers.pop();

            if (numbers.empty()) return firstNum;

            Integer secondNum = numbers.pop();
            String operand = stack.pop();

            int result = -1;

            if (operand.equals("*")) {
                result = firstNum * secondNum;
            } else if (operand.equals("/")) {
                result =  secondNum / firstNum;
            } else if (operand.equals("-")) {
                result =  - firstNum + secondNum;
            } else if (operand.equals("+")) {
                result = firstNum + secondNum;
            }

            boolean stackEmpty = stack.empty();
            if (stackEmpty) {
                return result;
            }

            stack.push(String.valueOf(result));
        }

        return 0;
    }
}
