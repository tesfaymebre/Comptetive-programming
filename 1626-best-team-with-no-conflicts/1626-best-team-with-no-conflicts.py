class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #bottom up dp solution
        age_score = sorted(zip(ages,scores))

        size = len(age_score)
        dp = [0] * size
        
        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                if age_score[j][1] >= age_score[i][1]:
                    dp[i] = max(dp[i], dp[j])
                    
            dp[i] += age_score[i][1]
            
        return max(dp)
        