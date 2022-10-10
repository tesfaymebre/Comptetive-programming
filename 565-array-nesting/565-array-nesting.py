class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(idx,seen):
            if idx in seen:
                return 0
            if idx in memo:
                return memo[idx]
            
            seen.add(idx)
            memo[idx] = 1 + dfs(nums[idx],seen)
            return memo[idx]
            
            
        ans = 0
        
        for i in range(len(nums)):
            ans = max(ans,dfs(i,set()))
            
        return ans