class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        sufix = [0]*(len(grid[0])+1)
        prefix = [0]
        
        for i in range(n-1,-1,-1):
            sufix[i] = sufix[i+1] + grid[0][i]
            
        for j in range(n):
            prefix.append(prefix[-1] + grid[1][j])
        
        robot2 = float('inf')
        
        for turn in range(n):
            remain1 = sufix[turn+1]
            remain2 = prefix[turn]
            posible_val = max(remain1,remain2)
            
            robot2 = min(robot2,posible_val)
            
        return robot2
        
        
        