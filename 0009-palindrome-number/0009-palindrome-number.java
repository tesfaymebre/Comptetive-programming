class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;

        int xCopy = x;
        int reversedX = 0;

        while (xCopy > 0){
            reversedX = reversedX * 10 + xCopy % 10;
            xCopy /= 10;
        }

        return x == reversedX;

    }
}