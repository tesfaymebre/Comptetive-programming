class Solution {
    public boolean check(int[] nums) {
        int size = nums.length;
        int count = 0;

        for (int i = 0; i < size - 1; i++){
            if (nums[i] > nums[i+1]){
                count++;
            } 
        }

        return (count == 0) || (count == 1 && nums[0] >= nums[size -1]);
    }
}