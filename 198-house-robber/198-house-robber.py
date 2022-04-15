class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + dp(i+2), dp(i+1))
            return memo[i]
        
        return dp(0)
    
    # solution 2 iterative
    
#     prev = 0
#         curr = 0
        
#         for x in nums:
#             temp = prev
#             prev = curr
#             curr = max(temp + x, curr)
            
#         return curr