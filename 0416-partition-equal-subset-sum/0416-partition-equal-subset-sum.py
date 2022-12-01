class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        
        def helper(idx,curr_total):
            if (idx,curr_total) not in memo:
            
                if curr_total == 0:
                    return True

                if idx == len(nums) or curr_total < 0:
                    return False

                memo[(idx,curr_total)] = helper(idx+1,curr_total-nums[idx]) or helper(idx+1,curr_total)
            
            return memo[(idx,curr_total)]
        
        total = sum(nums)
        
        if total&1 == 1:
            return False
        
        return helper(0,total//2)
        