class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix_sum = [0]*101
        
        for birth,death in logs:
            prefix_sum[birth%1950] += 1
            prefix_sum[death%1950] -= 1
            
        max_population = prefix_sum[0]
        year_idx = 0
        
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
            
            if max_population < prefix_sum[i]:
                max_population = prefix_sum[i]
                year_idx = i
                
        return year_idx + 1950
            
        