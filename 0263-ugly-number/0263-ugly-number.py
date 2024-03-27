class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        def keep_dividing(dividend, divisor):
            while dividend % divisor == 0:
                dividend //= divisor
            
            return dividend
        
        for divisor in [2,3,5]:
            n = keep_dividing(n, divisor)
            
        if n == 1:
            return True
        
        return False