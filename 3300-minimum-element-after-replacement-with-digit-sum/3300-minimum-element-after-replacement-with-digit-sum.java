class Solution {
    public int minElement(int[] nums) {
        int mini = Integer.MAX_VALUE;

        for (int num : nums){
            int current = 0;

            while (num > 0){
                current += num % 10;
                num /= 10;
            }

            mini = Math.min(mini, current);
        }

        return mini;
    }
}