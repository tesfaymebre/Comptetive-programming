class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            day_needed = 1
            i = 0
            temp_weight = 0
            
            while i < len(weights):
                temp_weight += weights[i]
                
                if temp_weight > mid:
                    day_needed += 1
                    temp_weight = weights[i]
                    
                i += 1
                
            return day_needed
        
        left,right = max(weights),sum(weights)
        temp = 0
        
        while left <= right:
            mid = left + (right - left)//2
            day_needed = check(mid)
           
            if day_needed <= days:
                temp = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return temp