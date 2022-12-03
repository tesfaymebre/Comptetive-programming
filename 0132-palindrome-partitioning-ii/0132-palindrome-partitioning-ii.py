class Solution:
    def minCut(self, s: str) -> int:
        
        @cache
        def isPalindrome(left,right):
            if left > right:
                return True
            if s[left] != s[right]:
                return False
            
            return isPalindrome(left+1,right-1)
        
        @cache
        def helper(left):
            if left == len(s):
                return 0
            
            count = float('inf')
            
            for right in range(left,len(s)):
                
                if isPalindrome(left,right):
                    count = min(count,1 + helper(right+1))
                    
            return count
        
        return helper(0)-1
        
                    
                