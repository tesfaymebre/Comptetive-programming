class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #top down solution
        memo = {}
        
        def dp(idx,amount):
            if (idx,amount) not in memo:
                if amount == 0:
                    return 1
                
                if idx == len(nums):
                    return 0
                
                
                count = 0
                for i in range(len(nums)):
                    if nums[i] <= amount:
                        count += dp(i,amount-nums[i])
                
                memo[(idx,amount)] = count
                
            return memo[(idx,amount)]
        
        return dp(0,target)