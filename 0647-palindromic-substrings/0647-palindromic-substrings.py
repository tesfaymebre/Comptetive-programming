class Solution:
    def countSubstrings(self, s: str) -> int:
        # bottom up dp solution little bit time optimized
        
        size = len(s)
        dp = [[False]*(size+1) for _ in range(size+1)]
        
        count = 0
        
        for left in range(size-1,-1,-1):
            for right in range(left,size):
                if s[left] == s[right]:
                    if right - left < 2:
                        dp[left][right] = True
                    else:
                        dp[left][right] = dp[left+1][right-1]
                        
                if dp[left][right]:
                    count += 1
                    
        return count
    
        """
        #bottom up dp solution
        
        size = len(s)
        
        dp = [[False]*(size+1) for _ in range(size+1)]
        
        for left in range(size-1,-1,-1):
            for right in range(left,size):
                if s[left] == s[right]:
                    if right - left > 1:
                        dp[left][right] = dp[left+1][right-1]
                    else:
                        dp[left][right] = True
                        
        count = 0
        
        for left in range(len(s)):
            for right in range(left,len(s)):
                if dp[left][right]:
                    count += 1  
                    
        return count"""
        
        """
        #top down dp solution
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
        """
        

        """
        # starting from center and expanding to both ways
         count = 0
        
        for center in range(len(s)):
            for right in [center,center+1]:
                left = center
                
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                    
        return count
        """