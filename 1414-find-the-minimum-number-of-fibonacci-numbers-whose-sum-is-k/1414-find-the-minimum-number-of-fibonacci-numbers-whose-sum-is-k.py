class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [0,1]
        
        while fib[-1] < k:
            fib.append(fib[-1]+fib[-2])
            
        count = 0
        
        for i in range(len(fib)-1,-1,-1):
            if fib[i] <= k:
                count += k//fib[i]
                k = k%fib[i]
                
            if k == 0:
                break
        
        return count
        