class Solution {
    public int helper(int[] start1, int[] duration1, int[] start2, int[] duration2){
        int total1 = Integer.MAX_VALUE;

        for (int i = 0; i < start1.length; i++){
            total1 = Math.min(total1, start1[i] + duration1[i]);
        }

        int total2 = Integer.MAX_VALUE;

        for (int j = 0; j < start2.length; j++){
            total2 = Math.min(total2, Math.max(total1, start2[j]) + duration2[j]);
        }

        return total2;
    }
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int land_water = helper(landStartTime, landDuration, waterStartTime, waterDuration);
        int water_land = helper(waterStartTime, waterDuration, landStartTime, landDuration);

        return Math.min(land_water, water_land);
    }
}