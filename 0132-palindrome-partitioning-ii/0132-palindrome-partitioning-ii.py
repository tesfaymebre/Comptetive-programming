class Solution:
    def minCut(self, s: str) -> int:
        
        def helper(left):
            if left not in memo:
                if left == len(s):
                    return 0

                count = float('inf')

                for right in range(left,len(s)):

                    if s[left:right+1] == s[left:right+1][::-1]:
                        count = min(count,1 + helper(right+1))

                memo[left] = count
                
            return memo[left]
        
        memo = {}
        
        return helper(0) - 1
        
                    
                