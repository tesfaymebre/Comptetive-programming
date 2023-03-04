class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        sufix = [0]*(len(grid[0])+1) # time :n+1 space : n + 1
        prefix = [0]
        
        """
        [[11,9,4]
        ,[1,6,7]]
        """
        for i in range(n-2,-1,-1):
            grid[0][i] += grid[0][i+1] #time : n
            
        for j in range(1,n):
            grid[1][j] += grid[1][j-1]
        
        robot2 = float('inf')
        
        for turn in range(n):
            remain1 = 0
            
            if turn < n - 1:
                remain1 = grid[0][turn+1]
                
            remain2 = 0
            
            if turn > 0:
                remain2 = grid[1][turn-1]
                
            posible_val = max(remain1,remain2)
            
            robot2 = min(robot2,posible_val)
            
        return robot2
        
        
        # time: O(n)
        #space: O(1)
        