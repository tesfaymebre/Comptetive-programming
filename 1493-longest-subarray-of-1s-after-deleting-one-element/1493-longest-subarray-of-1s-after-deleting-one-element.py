class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = [-1]
        
        for idx in range(len(nums)): 
            if nums[idx] == 0:
                zeros.append(idx)
                
        zeros.append(len(nums))
        
        if len(zeros) == 2:
            return len(nums)-1
                
        maxx = 0
        
        for i in range(1,len(zeros)-1):
            maxx = max(maxx,zeros[i+1] - zeros[i-1] - 2)
          
        return maxx
        