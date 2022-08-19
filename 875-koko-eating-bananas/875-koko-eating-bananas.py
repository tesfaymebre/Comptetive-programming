class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            hrs = 0
            
            for x in piles:
                hrs += math.ceil(x/mid)
            
            return hrs
        
        left,right = 1,max(piles)
        temp = 1
        
        while left <= right:
            mid = left + (right - left)//2
            hrs = check(mid)
            
            if hrs <= h:
                temp = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return temp