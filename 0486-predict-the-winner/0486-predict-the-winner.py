class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dp(i,j):
            if i == j:
                return nums[i]
           
            curr_score = max(nums[i] - dp(i+1,j),nums[j] - dp(i,j-1))
            return curr_score
        
        player_1_score = dp(0,len(nums)-1)
        
        return True if player_1_score >= 0 else False
        