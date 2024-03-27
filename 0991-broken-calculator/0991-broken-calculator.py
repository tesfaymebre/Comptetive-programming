class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        
        while target > startValue:
            if target % 2:
                target += 1
            else:
                target //= 2
                
            count += 1
            
        return count + startValue - target