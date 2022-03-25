class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        
        for i in range(len(nums)):
            largest = nums[i]
            smallest = nums[i]
            
            for j in range(i,len(nums)):
                largest = max(largest, nums[j])
                smallest = min(smallest, nums[j])
                total += largest - smallest
                
        return total