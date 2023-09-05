class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #top down solution
        memo = {}
        
        def dp(amount):
            if amount not in memo:
                if amount == 0:
                    return 1
                
                count = 0
                for i in range(len(nums)):
                    if nums[i] <= amount:
                        count += dp(amount-nums[i])
                
                memo[amount] = count
                
            return memo[amount]
        
        return dp(target)
        