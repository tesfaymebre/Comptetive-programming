class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        memo = {}
        
        def dp(idx,zeros):
            if (idx,zeros) not in memo:
                if idx == len(s) or zeros == 0:
                    return 0

                cur_flip = 0

                if s[idx] == '1':
                    cur_flip = min(zeros,1 + dp(idx+1,zeros))
                else:
                    cur_flip = dp(idx+1,zeros-1)
                
                memo[(idx,zeros)] = cur_flip
                
            return memo[(idx,zeros)]
                
        zeros = s.count('0')
        return dp(0,zeros)