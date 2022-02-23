class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        ans = 0
        ptr = 0
        prefix_sum = []
        
        prefix_sum.append(0)
        
        for i in range(len(nums)):
            
            prefix_sum.append(prefix_sum[-1] + nums[i])
            gap = (i - ptr) * nums[i] - (prefix_sum[i] - prefix_sum[ptr])
            
            while ptr < i and gap > k:
                
                ptr += 1
                gap = (i - ptr) * nums[i] - (prefix_sum[i] - prefix_sum[ptr])
                
            ans = max(ans, i - ptr + 1)
            
        return ans
        