class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def recur(x, n, mod):
            if n == 0:
                return 1
            elif n == 1:
                return x
            else:
                half = recur(x, n//2, mod)
                
                if n % 2 == 0:
                    return (half * half) % mod
             
                return ((half * half) % mod * x) % mod
      
        if n % 2 == 0:
            return ((recur(4, n//2, 10**9 + 7)) * (recur(5, n//2, 10**9 + 7))) % (10**9 + 7)
    
        return ((recur(4, n//2 ,10**9 + 7)) * (recur(5, 1 + n//2, 10**9 + 7))) % (10**9 + 7)