class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        
        while right > left:
            if s[left] != s[right]:
                return right - left + 1
            
            while left + 1 < right and s[left] == s[left + 1]:
                left += 1
                
            while right - 1 > left and s[right] == s[right - 1]:
                right -= 1
                
            left += 1
            right -= 1
                
        return right - left + 1