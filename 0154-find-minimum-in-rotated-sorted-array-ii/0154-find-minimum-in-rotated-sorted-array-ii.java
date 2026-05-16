class Solution {
    public int findMin(int[] nums) {
        int best = nums[0];
        int left = 0;
        int right = nums.length - 1;

        while (right > 0 && nums[right] == nums[right - 1]){
            right -= 1;
        }

        while (left <= right){
            int mid = left + (right - left) / 2;

            if (nums[left] <= nums[mid]){
                best = Math.min(best, nums[left]);
                left = mid + 1;
            } else {
                best = Math.min(best, nums[mid]);
                right = mid - 1;
            }
        }

        return best;
    }
}