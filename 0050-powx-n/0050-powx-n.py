class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        x = 1/x if n < 0 else x
        temp = self.myPow(x,abs(n)//2)
        
        return x * temp*temp if n%2 else temp * temp
        