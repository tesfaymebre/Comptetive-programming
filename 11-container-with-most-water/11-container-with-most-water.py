class Solution:
    def maxArea(self, height: List[int]) -> int:
        pt1 = 0
        pt2 = len(height) -1
        maxi_area = 0
        
        while True:
            curr_area = min(height[pt1],height[pt2])*abs(pt2 - pt1)
            maxi_area = max(maxi_area, curr_area)
            
            if pt1 == pt2:
                break
                
            if height[pt1] < height[pt2]:
                pt1 += 1
            else:
                pt2 -= 1
                
        return maxi_area
                
                