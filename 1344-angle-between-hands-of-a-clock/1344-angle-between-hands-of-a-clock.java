class Solution {
    public double angleClock(int hour, int minutes) {
        if (hour == 12) hour = 0;

        double hrPosition = (hour * 5) + (minutes / 60.0) * 5.0;

        return Math.min(Math.abs(minutes - hrPosition), Math.min(60 - minutes + hrPosition, 60 - hrPosition + minutes)) * 6;
        
    }
}