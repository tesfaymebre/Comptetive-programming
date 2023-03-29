class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
                
        duplicates = []
        
        for j in range(len(nums)):
            if j+1 != nums[j]:
                duplicates.append(nums[j])
                
        return duplicates