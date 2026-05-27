class Solution {
    public int numberOfSpecialChars(String word) {
        int[] lastIdxLower = new int[26];
        int[] firstIdxUpper = new int[26];

        Arrays.fill(lastIdxLower, -1);
        Arrays.fill(firstIdxUpper, -1);

        for (int i=0; i < word.length(); i++){
            char c = word.charAt(i);

            if (Character.isLowerCase(c)){
                lastIdxLower[c - 'a'] = i;
            } else if (firstIdxUpper[c - 'A'] == -1){
                firstIdxUpper[c - 'A'] = i;
            }
        }

        int count = 0;

        for (int j = 0; j < 26; j++){
            if (lastIdxLower[j] != -1 && lastIdxLower[j] < firstIdxUpper[j]){
                count ++;
            }
        }

        return count;
    }
}