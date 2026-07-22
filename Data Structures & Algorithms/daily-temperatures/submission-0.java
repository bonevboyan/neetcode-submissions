class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            result[i] = 0;
        }

        for (int i = 0; i < temperatures.length; i++) {
            for (int j = i; j < temperatures.length; j++) {
                int temp1 = temperatures[i];
                int temp2 = temperatures[j];

                if (temp2 > temp1) {
                    result[i] = j - i;
                    break;
                }
            }
        }

        return result;
    }

}
