class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        i ,j= 0,0
        
        
        while i < len(prices):
            while  j < len(prices) - 1 and prices[j] - prices[j+1] == 1:
                j +=1
            count = j - i + 1
            ans += count*(count + 1)//2
            i = j+1
            j +=1
           
        
        return ans
                