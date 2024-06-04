class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        flag = False
        
        for key,val in freq.items():
            if val & 1:
                res += val - 1
                flag = True
            else:
                res += val
        
        return res + 1 if flag else res