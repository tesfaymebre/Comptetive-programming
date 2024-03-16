class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        memo[0] = -1
        max_len = 0
        running_sum = 0
        
        for i,num in enumerate(nums):
            running_sum += num if num else -1
            
            if running_sum in memo:
                max_len = max(max_len, i - memo[running_sum])
            else:
                memo[running_sum] = i
                
        return max_len