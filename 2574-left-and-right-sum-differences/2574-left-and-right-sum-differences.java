class Solution {
    public int[] leftRightDifference(int[] nums) {
        int[] answer = new int[nums.length];
        int total = Arrays.stream(nums).sum();
        int running_sum = 0;

        for (int i=0; i < nums.length; i++){
            answer[i] = Math.abs(2*running_sum - total + nums[i]);
            running_sum += nums[i];
        }

        return answer;
    }
}