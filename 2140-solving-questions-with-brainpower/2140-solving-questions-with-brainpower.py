class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        def dp(idx):
            if idx not in memo:
                if idx >= len(questions):
                    return 0

                score = questions[idx][0] + dp(idx + questions[idx][1] + 1)
                score = max(score,dp(idx+1))

                memo[idx] = score
                
            return memo[idx]
        
        memo = {}
        return dp(0)