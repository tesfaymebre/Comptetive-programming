class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sliding window approach
        nums.sort()
        
        max_freq = 0
        curr_window_sum = 0
        left = 0
        
        for right in range(len(nums)):
            curr_window_sum += nums[right]
            
            while left <= right and (right - left + 1)*nums[right] - curr_window_sum > k:
                curr_window_sum -= nums[left]
                left += 1
                
            max_freq = max(max_freq,right - left +1)
            
        return max_freq
                
        
        """
        # prefix sum approach
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
        
        """