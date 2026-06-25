class Solution {
    public int countMajoritySubarrays(int[] nums, int target) {
        int count = 0;

        for (int i = 0; i < nums.length; i++){
            int curr = 0;

            for (int j = i; j < nums.length; j++){
                if (nums[j] == target) curr += 1;
                else curr -= 1;

                if (curr > 0) count += 1;
            }
        }

        return count;
    }
}