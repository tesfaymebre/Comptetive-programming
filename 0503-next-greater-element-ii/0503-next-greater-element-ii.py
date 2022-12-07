class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        result = [-1]*n
        
        for i in range(n*2):
            while stack and nums[stack[-1]] < nums[i%n]:
                idx = stack.pop()
                result[idx] = nums[i%n]
                
            stack.append(i%n)
            
        return result