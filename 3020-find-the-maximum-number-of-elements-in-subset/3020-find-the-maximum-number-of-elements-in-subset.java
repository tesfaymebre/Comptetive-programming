class Solution {
    public int maximumLength(int[] nums) {
       Map<Integer, Integer> freq = new HashMap<>(); 

       for (int num : nums){
        freq.put(num, freq.getOrDefault(num, 0) + 1);
       }

        List<Integer> uniqueNums = new ArrayList<>(freq.keySet());
        uniqueNums.sort(Collections.reverseOrder());
        int maxi = freq.getOrDefault(1,0) % 2 == 1 ? freq.get(1) : freq.getOrDefault(1,0) - 1;

       for (int num: uniqueNums){
        if (freq.get(num) > 0){
            int curr = num;
            freq.put(num, 0);
            int count = 1;

            while (true){
                int temp = (int) Math.sqrt(curr);

                if (temp * temp == curr && freq.getOrDefault(temp,0) >= 2){
                    count += 2;
                    freq.put(temp,0);
                    curr =temp;
                } else {
                    break;
                }
            }

            maxi = Math.max(maxi,count);
        }
       }

       return maxi;
    }
}