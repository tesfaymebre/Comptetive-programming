class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
       
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if bin(nums[j]).count('1') == bin(nums[j-1]).count('1') and nums[j] < nums[j-1]:
                    nums[j],nums[j-1] = nums[j-1],nums[j]
      
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False

        return True