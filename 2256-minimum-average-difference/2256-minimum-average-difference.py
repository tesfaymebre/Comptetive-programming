class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]
        
        for val in nums:
            prefix_sum.append(prefix_sum[-1]+val)
            
        idx_min = 0
        min_val = float('inf')
        
        for i in range(n):
            if i != n-1:
                average = abs(prefix_sum[i+1] // (i+1) - (prefix_sum[-1]-prefix_sum[i+1])//(n-i-1))
            else:
                average = prefix_sum[i+1] // (i+1)
                
            if min_val > average:
                idx_min = i
                min_val = average
               
        return idx_min