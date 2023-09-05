class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #bottom up dp solution
        n = len(nums)
        dp = [[0]*(target+1) for _ in range(n)]
        
        #base case
        for i in range(n):
            dp[i][0] = 1
        
        for amount in range(1,target+1):
            for idx in range(n):
                count = 0
                
                for i in range(n):
                    if nums[i] <= amount:
                        count += dp[i][amount-nums[i]]
                        
                dp[idx][amount] = count
                
        return dp[0][target]
    
        """
        #top down solution
        memo = {}
        
        def dp(idx,amount):
            if (idx,amount) not in memo:
                if amount == 0:
                    return 1
                
                count = 0
                for i in range(len(nums)):
                    if nums[i] <= amount:
                        count += dp(i,amount-nums[i])
                
                memo[(idx,amount)] = count
                
            return memo[(idx,amount)]
        
        return dp(0,target)
        """