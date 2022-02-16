class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1 = [1]
        l2 = [1]
        
        for x in nums:
            l1.append(l1[-1] * x)
            
        for i in range(len(nums)-1,-1,-1):
            l2.append(l2[-1] * nums[i])
            
        l2 = l2[::-1]
        
        for j in range(len(nums)):
            nums[j] = l1[j] * l2[j+1]
            
        return nums