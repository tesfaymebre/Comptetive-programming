class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
      
        def helper(radius):
            i = 0
            j = 0
            
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= radius:
                    i += 1
                else:
                    j += 1
                    
            if i < len(houses):
                return False
            
            return True
        
        houses.sort()
        heaters.sort()
        
        left = 0
        right = max(houses[-1],heaters[-1])
        best = right
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if helper(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return best
            