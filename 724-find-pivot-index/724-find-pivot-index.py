class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = [0]
        
        for i in range(len(nums)):
            sums.append(sums[-1] + nums[i])
        
        for j in range(len(sums)-1):
            if sums[j] == sums[-1] - sums[j+1]:
                return j 
            
        return -1
        