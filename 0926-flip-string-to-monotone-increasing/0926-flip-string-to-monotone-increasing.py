class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        def dp(idx,zeros):
            if idx == len(s) or zeros == 0:
                return 0
            
            cur_flip = 0
            
            if s[idx] == '1':
                cur_flip = min(zeros,1 + dp(idx+1,zeros))
            else:
                cur_flip = dp(idx+1,zeros-1)
                
            return cur_flip
                
        zeros = s.count('0')
        return dp(0,zeros)