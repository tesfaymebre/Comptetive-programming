class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        i, count = 0, 1
        
        while i < len(prices):
            if i < len(prices) -1 and prices[i] - prices[i+1] == 1:
                count += 1
            else:
                ans += count*(count + 1)//2
                count = 1
                
            i += 1
            
        return ans
                