class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l2 = [1]
            
        for i in range(len(nums)-1,-1,-1):
            l2.append(l2[-1] * nums[i])
            
        l2.pop()    
        l2 = l2[::-1]
        pre = 1
        
        for j in range(len(nums)):
            l2[j] = pre * l2[j]
            pre *= nums[j]
            
        return l2
