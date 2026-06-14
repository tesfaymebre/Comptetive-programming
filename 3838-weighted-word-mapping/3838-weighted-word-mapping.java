class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder ans = new StringBuilder(words.length);

        for (String word : words){
            int curr_total = 0;

            for (int i = 0; i < word.length(); i++){
                curr_total += weights[word.charAt(i) - 'a'];
            }

            ans.append((char) (25 - (curr_total % 26) + 'a'));
        }

        return ans.toString();
    }
}