class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        max_value = 10**10
        
        left = 0
        right = 10**10
        
        while left <= right:
            mid = left + (right-left)//2
            
            non_div_by1 = mid - mid//divisor1
            non_div_by2 = mid - mid//divisor2
            non_div_by_both = mid - mid//lcm(divisor1,divisor2)
            total_count = uniqueCnt1 + uniqueCnt2
            
            if uniqueCnt1 <= non_div_by1 and uniqueCnt2 <= non_div_by2 and total_count <= non_div_by_both:
                max_value = min(max_value,mid)
                right = mid - 1
            else:
                left = mid + 1
              
        return max_value