class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] freq = new int[26];

        for (char c : text.toCharArray()) {
            freq[c - 'a']++;
        }

        freq['l' - 'a'] /= 2;
        freq['o' - 'a'] /= 2;
        int mini = Integer.MAX_VALUE;

        for (char c : "balon".toCharArray()){
            mini = Math.min(mini, freq[c - 'a']);
        }

        return mini;
    }
}