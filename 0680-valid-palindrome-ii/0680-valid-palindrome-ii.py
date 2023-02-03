class Solution:
    def validPalindrome(self, s: str) -> bool:
        reverse = s[::-1]
        
        if s == reverse:
            return True
        
        for i in range(len(s)):
            if s[i] != reverse[i]:
                new_s = s[:i] + s[i+1:]
                new_reverse = reverse[:i] + reverse[i+1:]
                
                if new_s == new_s[::-1] or new_reverse == new_reverse[::-1]:
                    return True
                
                return False
            
        return False