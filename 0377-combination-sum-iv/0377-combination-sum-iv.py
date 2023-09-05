class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #bottom up dp solution
        n = len(nums)
        dp = [0]*(target+1)
        
        #base case
        dp[0] = 1
        
        for amount in range(1,target+1):
            for i in range(n):
                if nums[i] <= amount:
                    dp[amount] += dp[amount-nums[i]]

        return dp[target]
        
        """
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
        
        """