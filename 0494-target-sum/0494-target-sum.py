class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dp(pos,cur_total):
            if pos == len(nums):
                if cur_total == target:
                    return 1
                else:
                    return 0
            
            if (pos,cur_total) in memo:
                return memo[(pos,cur_total)]
            
            count = 0
            
            count += dp(pos+1,cur_total+nums[pos]) + dp(pos+1,cur_total-nums[pos])
            memo[(pos,cur_total)] = count
            return memo[(pos,cur_total)]
        
        return dp(0,0)