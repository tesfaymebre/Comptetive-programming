class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # solution 2
        prefix = defaultdict(int)
        prefix[0] = 1
        
        count = 0
        running_sum = 0
        
        for num in nums:
            running_sum += num
            
            count += prefix[running_sum - goal]
            prefix[running_sum] += 1
            
        return count
            
        
        """
        # solution 1 
        
        def atMost(target):
            if target < 0: 
                return 0
            
            count = 0
            left = 0
            for right in range(len(nums)):
                target -= nums[right]
                
                while target < 0:
                    target += nums[left]
                    left += 1
                    
                count += right - left + 1
                
            return count
        
        return atMost(goal) - atMost(goal - 1)
        """