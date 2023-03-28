class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i]-1 != i and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
                
        result = []
        
        for j in range(len(nums)):
            if nums[j] != j+1:
                result.append(j+1)
                
        return result