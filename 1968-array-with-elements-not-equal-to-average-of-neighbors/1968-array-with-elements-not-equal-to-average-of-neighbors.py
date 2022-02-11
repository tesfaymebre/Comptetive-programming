class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        arrangedArr = [] 
        
        n = len(nums)//2
        if len(nums)%2 == 1:
            n += 1
            
        for i in range(n):
            arrangedArr.append(nums[i])
            if i+n < len(nums):
                arrangedArr.append(nums[i+n])
    
        return arrangedArr