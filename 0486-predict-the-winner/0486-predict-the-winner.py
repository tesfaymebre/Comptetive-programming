class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dp(i,j):
            if i == j:
                return nums[i]
           
            ans = max(nums[i] - dp(i+1,j),nums[j] - dp(i,j-1))
            return ans
        
        ans = dp(0,len(nums)-1)
        if ans >= 0:
            return True
        else:
            return False