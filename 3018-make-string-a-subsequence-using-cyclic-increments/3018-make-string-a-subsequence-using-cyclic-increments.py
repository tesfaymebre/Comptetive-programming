class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx = 0
        ord_a = ord('a')

        for c in str1:
            if c == str2[idx] or (c == 'z' and str2[idx] == 'a') or chr(ord(c) + 1) == str2[idx]:
                idx += 1

            if idx == len(str2):
                return True

        return False