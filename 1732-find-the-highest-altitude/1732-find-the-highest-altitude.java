class Solution {
    public int largestAltitude(int[] gain) {
        int maxAltitude = 0;
        int runningSum = 0;

        for (int x : gain){
            runningSum += x;
            maxAltitude = Math.max(maxAltitude, runningSum);
        }

        return maxAltitude;
    }
}