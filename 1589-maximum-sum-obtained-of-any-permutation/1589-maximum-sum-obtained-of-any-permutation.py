class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)
        
        for st,end in requests:
            prefix_sum[st] += 1
            prefix_sum[end+1] -= 1
            
        for j in range(1,n+1):
            prefix_sum[j] += prefix_sum[j-1]
      
        prefix_sum.sort()
        nums.sort()

        total = 0
        for i in range(1,n+1):
            total += (nums[i-1] * prefix_sum[i])
            
        return total % (10**9 + 7)