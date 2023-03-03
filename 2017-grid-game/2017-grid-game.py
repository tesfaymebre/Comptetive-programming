class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix_sum = [[0]*(len(grid[0])+1) for _ in range(3)]
        
        rows = len(prefix_sum)
        cols = len(prefix_sum[0])
        
        for r in range(1,rows):
            for c in range(1,cols):
                prefix_sum[r][c] = prefix_sum[r-1][c] + prefix_sum[r][c-1] \
                                  - prefix_sum[r-1][c-1] + grid[r-1][c-1]
       
        robot2 = float('inf')
        
        for i in range(1,cols):
            remain_path_sum1 = prefix_sum[2][i-1] - prefix_sum[1][i-1]
            remain_path_sum2 = prefix_sum[1][cols-1] - prefix_sum[1][i]
            
            if robot2 > max(remain_path_sum1,remain_path_sum2):
                robot2 = max(remain_path_sum1,remain_path_sum2)
        
        return robot2
            
        
                