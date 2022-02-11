class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:
            x = 1/x if n < 0 else x
            n = abs(n)
            temp = self.myPow(x,n//2)
            
            if n%2 == 0:
                return temp * temp
            return x * temp*temp