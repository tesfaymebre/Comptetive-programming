class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        stack = []
        
        for num in nums:
            while stack and stack[-1] >= num:
                stack.pop()
            
            stack.append(num)
            
            if len(stack) >= 2:
                max_diff = max(max_diff,stack[-1] - stack[0])
                
        return max_diff
            