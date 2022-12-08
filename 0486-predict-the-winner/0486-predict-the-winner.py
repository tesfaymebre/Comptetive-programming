class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        #top down dp solution
        
        def dp(i,j):
            if (i,j) not in memo:
                if i == j:
                    return nums[i]

                curr_score = max(nums[i] - dp(i+1,j),nums[j] - dp(i,j-1))
                memo[(i,j)] = curr_score
                
            return memo[(i,j)]
        
        memo = {}
        player_1_score = dp(0,len(nums)-1)
        
        return True if player_1_score >= 0 else False
        
        