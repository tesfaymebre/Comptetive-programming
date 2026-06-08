class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        List<Integer> left_side = new ArrayList<>();
        List<Integer> equals = new ArrayList<>();
        List<Integer> right_side = new ArrayList<>();
        
        for (int i=0; i < nums.length; i++){
            if (nums[i] < pivot) left_side.add(nums[i]);
            else if (nums[i] > pivot) right_side.add(nums[i]);
            else equals.add(nums[i]);
        }

        left_side.addAll(equals);
        left_side.addAll(right_side);
        
        int[] answer = left_side.stream().mapToInt(i -> i).toArray();
        return answer;

    }
}