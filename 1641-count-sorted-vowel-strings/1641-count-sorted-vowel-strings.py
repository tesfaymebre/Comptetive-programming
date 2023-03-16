class Solution:
    def countVowelStrings(self, n: int) -> int:
        num_vowels = 5
        memo = {}
        
        def dp(idx,size):
            if (idx,size) not in memo:
                if size == n:
                    return 1

                if size > n:
                    return 0

                count = 0
                for i in range(idx,num_vowels):
                    count += dp(i,size + 1)

                memo[(idx,size)] = count
                
            return memo[(idx,size)]
        return dp(0,0)