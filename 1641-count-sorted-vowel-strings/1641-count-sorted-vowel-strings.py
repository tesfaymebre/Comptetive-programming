class Solution:
    def countVowelStrings(self, n: int) -> int:
        num_vowels = 5
        
        def dp(idx,size):
            if size == n:
                return 1
            
            if size > n:
                return 0
            
            count = 0
            for i in range(idx,num_vowels):
                count += dp(i,size + 1)
                
            return count
        
        return dp(0,0)