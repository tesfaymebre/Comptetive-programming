class Solution {
    public long sumAndMultiply(int n) {
        int x = 0;
        int sum = 0;
        int pow10 = 0;

        while (n > 0){
            int temp = n % 10;
            sum += temp;

            if (temp > 0){
                x += temp * Math.pow(10, pow10);
                pow10 += 1;
            }

            n /= 10;
        }

        return (long) x * sum;
    }
}