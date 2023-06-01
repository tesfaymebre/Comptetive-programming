class Solution:
    def rob(self, nums: List[int]) -> int:
        #top down dp solution
        
        def dp(idx,zero_idx):
            if (idx,zero_idx) not in memo:
                if idx >= len(nums):
                    return 0
                
                if idx == len(nums) - 1:
                    if zero_idx:
                        return 0
                    
                    return nums[idx]

                pick = nums[idx]
                
                if idx == 0:
                    pick += dp(idx+2,True)
                else:
                    pick +=dp(idx+2,zero_idx)
                    
                not_pick = dp(idx+1,zero_idx)

                memo[(idx,zero_idx)] = max(pick,not_pick)
                
            return memo[(idx,zero_idx)]
        
        memo = {}
        return dp(0,False)