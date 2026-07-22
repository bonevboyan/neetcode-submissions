class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];
        Stack<Integer> indices = new Stack<>();
        indices.push(0);

        for (int i = 1; i < n; i++) {
            int currentTemp = temperatures[i];

            while (!indices.isEmpty() && currentTemp > temperatures[indices.peek()]) {
                int idx = indices.pop();
                result[idx] = i - idx;
            }

            indices.push(i);
        }

        return result;




        // int[] result = new int[temperatures.length];

        // for (int i = 0; i < temperatures.length; i++) {
        //     result[i] = 0;
        // }

        // for (int i = 0; i < temperatures.length; i++) {
        //     for (int j = i; j < temperatures.length; j++) {
        //         int temp1 = temperatures[i];
        //         int temp2 = temperatures[j];

        //         if (temp2 > temp1) {
        //             result[i] = j - i;
        //             break;
        //         }
        //     }
        // }

        // return result;
    }

}
