class Solution {
    public char processStr(String s, long k) {
        long size = 0;

        for (char c : s.toCharArray()){
            if (c == '*'){
                if (size > 0) size -= 1;
            } else if (c == '#'){
                size *= 2;
            } else if (c == '%'){
                continue;
            } else {
                size += 1;
            }
        }

        if (k + 1 > size) return '.';

        for (int i = s.length() - 1; i > -1; i--){
            char c = s.charAt(i);
            if (c == '*'){
                size += 1;
            } else if (c == '#'){
                if (k + 1 > size / 2){
                    k -= size / 2;
                }
                size /= 2;
            } else if (c == '%'){
                k = size - k - 1;
            } else {
                if (size == k + 1) return c;

                size -= 1;
            }
        }

        return '.';
    }
}