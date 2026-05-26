class Solution {
    public int numberOfSpecialChars(String word) {
        Set<Character> freq = new HashSet<>();

        for (char c : word.toCharArray()){
            freq.add(c);
        }

        int count = 0;

        for (char c : freq){
            if (Character.isLowerCase(c) && freq.contains(Character.toUpperCase(c))) count ++;
        }

        return count;
    }
}