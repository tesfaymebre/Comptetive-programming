class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        trap = 0
        
        for i,h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                temp = height[stack.pop()]
                
                if stack:
                    w = i - stack[-1] - 1
                    trap += (min(height[stack[-1]],h) - temp) * w
                    
            stack.append(i)
        
        return trap