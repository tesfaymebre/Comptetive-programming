class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        
        def is_palindrome(left,right):
            if (left,right) not in memo:
                if left > right:
                    return True

                if s[left] != s[right]:
                    return False

                memo[(left,right)] = is_palindrome(left+1,right-1)
                
            return memo[(left,right)]
        
        count = 0
        
        for left in range(len(s)):
            for right in range(left,len(s)):
                if is_palindrome(left,right):
                    count += 1
                    
                    
        return count