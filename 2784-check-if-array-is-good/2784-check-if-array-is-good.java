class Solution {
    public boolean isGood(int[] nums) {
        int len = nums.length;
        int[] freq = new int[len];

        for (int num : nums) {
            if (num >= len) return false;

            freq[num]++;

            if (num == len - 1) continue;

            if (freq[num] != 1) return false;
        }

        return freq[len-1] == 2;
    }
}