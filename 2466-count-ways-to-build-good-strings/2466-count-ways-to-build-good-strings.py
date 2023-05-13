class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        def dp(size):
            if size not in memo:
                if size > high:
                    return 0
                
                count =0 
                if size >=low and size <= high:
                    count +=1
               
                pick_zero = dp(size+zero)

                pick_one = dp(size+one)
                memo[size] = (pick_zero + pick_one + count) % (10**9+7)
            
            return memo[size] 
        
        memo = {}
        return dp(0)
            