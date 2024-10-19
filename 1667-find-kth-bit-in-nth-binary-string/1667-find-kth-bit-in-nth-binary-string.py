class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def recur(n, k):
            ans = ["0","1","1"]
            mid = 2 **(n - 1) - 1
            
            if n == 0:
                return "0"
            elif n == 1:
                return ans[k]
            elif k == mid:
                return "1"
            elif k < mid:
                return recur(n-1, k)
            else: 

                if recur(n, 2*mid-k) == "0":
                    return "1"
                else:
                    return "0"
                
        return recur(n, k-1)